var express = require("express");
var router = express.Router();
var Campground = require("../models/campground");
var middleware = require("../middleware");   // automatically require index.js

router.get("/", (req, res) => {
   // Get all campgrounds form DB
   Campground.find({}, (err, allCampgrounds) => {
      if (err) {
         console.log("err");
      } else {
         res.render("campgrounds/index", {campgrounds: allCampgrounds});
      }
   });
});

// Create Route
router.post("/", middleware.isLoggedIn, (req, res) => {
   // get data from form and add to campgrounds array
   var name = req.body.name;
   var price = req.body.price;
   var image = req.body.image;
   var desc = req.body.description;
   var author = {
      id: req.user._id,
      username: req.user.username
   }
   var newCampground = {name: name, price: price, image: image, description: desc, author:author};
   // Create a new campground and save to DB
   Campground.create(newCampground, (err, newlyCreated) => {
      if (err) {
         console.log(err);
      } else {
         // redirect back to campgrounds page
         res.redirect("/campgrounds");
      }
   });
});

router.get("/new", middleware.isLoggedIn, (req, res) => {
  res.render("campgrounds/new"); 
});

// SHOW - shows more info about one campground
// order is important since you don't want this grabbing /new
router.get("/:id", (req, res) => {
   Campground.findById(req.params.id).populate("comments").exec( (err, foundCampground) => {
      if (err) {
         console.log(err);
      } else {
         res.render("campgrounds/show", {campground: foundCampground});
      }
   });
});

// EDIT campground Route
router.get("/:id/edit", middleware.checkCampgroundOwnership, (req, res) => {
   Campground.findById(req.params.id, (err, foundCampground) => {
      res.render("campgrounds/edit", {campground: foundCampground});         
   });
});

// Update Campground Route
router.put("/:id", middleware.checkCampgroundOwnership, (req, res) => {
   // find and update the correct campground
   Campground.findByIdAndUpdate(req.params.id, req.body.campground, (err, updatedCampground) => {
      if (err) {
         res.redirect("/campgrounds");
      } else {
         res.redirect("/campgrounds/" + req.params.id);
      }
   });
   // redirect somewhere (show page)
});

// Destroy Route
router.delete("/:id", middleware.checkCampgroundOwnership, (req, res) => {
   Campground.findByIdAndRemove(req.params.id, (err) => {
      if (err) {
         res.redirect("/campgrounds");
      } else {
         res.redirect("/campgrounds");
      }
   })
})

module.exports = router;