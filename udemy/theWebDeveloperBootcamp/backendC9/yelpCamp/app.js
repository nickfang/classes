var express = require("express");
var app = express();
var bodyParser = require("body-parser");
var mongoose = require("mongoose");
var flash = require("connect-flash");
var passport = require("passport");
var LocalStrategy = require("passport-local");
var methodOverride = require("method-override");
var Campground = require("./models/campground");
var Comment = require("./models/comment");
var User = require("./models/user");
var seedDB = require("./seed");

var commentRoutes    = require("./routes/comments");
var campgroundRoutes = require("./routes/campgrounds");
var indexRoutes      = require("./routes/index");

mongoose.connect("mongodb://localhost/yelp_camp");
app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));
app.use(methodOverride("_method"));
app.use(flash());
// seedDB(); // seed the database
      
// Passport Configuration
app.use(require("express-session")({
   secret: "this is a phrase that the passwords are derived from",
   resave: false,
   saveUninitialized:false
}));
app.use(passport.initialize());
app.use(passport.session());
passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());
// Middle ware that passes currentUser into all ejs so we don't have to do it manually.
app.use( (req, res, next) => {
   res.locals.currentUser = req.user;
   res.locals.error = req.flash("error");
   res.locals.success = req.flash("success");
   next();
});

app.use("/", indexRoutes);
app.use("/campgrounds", campgroundRoutes);
app.use("/campgrounds/:id/comments", commentRoutes);

app.listen(process.env.PORT, process.env.IP, () => {
   console.log("The YelpCamp Server Has Started.");
});

// REST (Representational State Transfer)  a mapping between HTTP routes and CRUD (Create, Read, Update and Destroy)
// 
// 7 Routes
//    Name        url            verb        desc.
//    =============================================================================
//  - INDEX       /dogs          GET         Display a list of all dog
//  / NEW         /dogs/new      GET         Displays for to make a new dog
//  \ CREATE      /dogs          POST        Add new dog to DB
//  - SHOW        /dogs/:id      GET         Shows info about one dog
//  / EDIT        /dogs/:id/edit GET         Show edit form for one dog
//  \ UPDATE      /dogs/:id      PUT         Update a particular dog, then redirect somewhere
//  - DESTROY     /dogs/:id      DELETE      Delete a particular dog, then redirect somewhere

// CRUD
//
// CREATE
// READ     /allBlogs
// UPDATE   /updateBlog/:id
// DESTROY  /destroy/:id


// MongoDB notes
//
// To find a document that doesn't contain an element:
//    db.campgrounds.find({name: "Reimers", description: {$exists: false}})

// Comment routes
//
// NEW      campgrounds/:id/comments/new
// CREATE   campgrounds/:id/comments