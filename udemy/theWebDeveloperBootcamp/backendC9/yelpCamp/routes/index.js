var express = require("express");
var router = express.Router();
var passport = require("passport");
var User = require("../models/user");

router.get("/", (req, res) => {
   res.render("landing");
});


// Auth Routes
router.get("/register", (req, res) => {
   res.render("register");
});

// handle sign up logic  -  If you try to register the same username and password, you'll get an error.  Get that automatically from 
router.post("/register", (req, res) => {
   var newUser = new User({username: req.body.username});
   User.register(newUser, req.body.password, (err, user) => {
      if (err) {
         return res.render("register", {"error": err.message});
      }
      passport.authenticate("local")(req, res, () => {
         req.flash("success", "Welcome to YelpCamp " + user.username);
         res.redirect("/campgrounds");
      });
   });
});

// Login Routes
router.get("/login", (req, res) => {
   res.render("login");
});

router.post("/login", passport.authenticate("local", 
   {                                            // This is a middle ware.
      successRedirect: "/campgrounds",
      failureRedirect: "/login"
   }), (req, res) => {
});

// Logout Routes
router.get("/logout", (req, res) => {
   req.logout();
   req.flash("success", "Logged you out!");
   res.redirect("/campgrounds");
});

module.exports = router;