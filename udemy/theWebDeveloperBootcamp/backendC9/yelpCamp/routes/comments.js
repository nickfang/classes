var express = require("express");
var router = express.Router({mergeParams: true});  // need to make sure the :id in the route is used correctly
var Campground = require("../models/campground");
var Comment = require("../models/comment");
var middleware = require("../middleware");

// Comments Routes

router.get("/new", middleware.isLoggedIn, (req, res) => {
   Campground.findById(req.params.id, (err, campground) => {
      if (err) {
         console.log(err);
      } else {
         res.render("comments/new", {campground: campground});
      }
   });
});

router.post("/", middleware.isLoggedIn, (req, res) => {
   Campground.findById(req.params.id, (err, campground) => {
      if (err) { 
         console.log(err);
         res.redirect("/campgrounds");
      } else {
         Comment.create(req.body.comment, (err, comment) => {
            if (err) {
               req.flash("error", "Something went wrong")
               console.log(err);
            } else {
               // add useranme and id to comment
               comment.author.id = req.user._id;
               comment.author.username = req.user.username;
               // save comment
               comment.save();
               campground.comments.push(comment);
               campground.save();
               req.flash("success", "Successfully added comment.");
               res.redirect("/campgrounds/" + campground._id);
            }
         });
      }
   });
});

// Comment Edit Route
router.get("/:commentId/edit", middleware.checkCommentOwnership, (req, res) => {
   Comment.findById(req.params.commentId, (err, foundComment) => {
      if (err) {
         res.redirect("back", {"error": err.message});
      } else {
         res.render("comments/edit", {campground_id: req.params.id, comment: foundComment});      
      }
   });
});

// Comment Update
router.put("/:commentId/", middleware.checkCommentOwnership, (req, res) => {
   Comment.findByIdAndUpdate(req.params.commentId, req.body.comment, (err, updatedComment) => {
      if (err) {
         res.redirect("back");
      } else {
         res.redirect("/campgrounds/"+ req.params.id);
      }
   });
});

// Comment Destroy
router.delete("/:commentId", middleware.checkCommentOwnership, (req, res) => {
   Comment.findByIdAndRemove(req.params.commentId, (err) => {
      if (err) {
         res.redirect("back");
      } else {
         req.flash("succes", "Comment deleted.");
         res.redirect("/campgrounds/" + req.params.id);
      }
   })
});


module.exports = router;