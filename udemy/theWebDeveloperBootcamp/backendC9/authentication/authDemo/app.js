var express = require("express")
var mongoose = require("mongoose");
var passport = require("passport");
var bodyParser = require("body-parser");
var User = require("./models/user");
var LocalStrategy = require("passport-local");
var passportLocalMongoose = require("passport-local-mongoose");

mongoose.connect("mongodb://localhost/auth_demo_app");

var app = express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended: true}));
app.use(require("express-session")({
   secret: "this is a secret",
   resave: false,
   saveUninitialized: false
}));
app.use(passport.initialize());
app.use(passport.session());

passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());  // User.serializeUser is from user.js passportLocal Mongoose
passport.deserializeUser(User.deserializeUser());

//---------------------------------------------------------------------------------------------------------------
// Routes
//---------------------------------------------------------------------------------------------------------------

app.get("/", (req, res) => {
   res.render("home");
});

app.get("/secret", isLoggedIn, (req, res) => {
   res.render("secret");
});

// Auth Routes

app.get("/register", (req, res) => {
   res.render("register");
});

app.post("/register", (req, res) => {
   User.register(new User({username: req.body.username}), req.body.password, (err, user) => {
      if (err) {
         console.log(err);
         return res.render("register");
      }
      passport.authenticate("local")(req, res, () => {
         res.redirect("/secret");   
      });
   });
});

// Login Routes
// render login form
app.get("/login", (req, res) => {
   res.render("login");
});
// login logic
// middleware - code that runs before our callback
app.post("/login", passport.authenticate("local", {
      successRedirect: "/secret",
      failureRedirect: "/login"
   }), (req, res) => {
});

// Logout Route
app.get("/logout", (req, res) => {
   req.logout();
   res.redirect("/");
})

function isLoggedIn(req, res, next) {
   if (req.isAuthenticated()) {
      return next();
   }
   res.redirect("/login");
}

app.listen(process.env.PORT, process.env.IP, () => {
   console.log("Server Started!");
});