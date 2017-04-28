var mongoose = require("mongoose");
var Campground = require("./models/campground");
var Comment = require("./models/comment");
var User = require("./models/user");

var data = [
   {
      name: "Enchanted Rock",
      image: "http://www.visitfredericksburgtx.com/wp-content/uploads/2011/06/Enchanted-Rock-State-Natural-Area-1-326x216.jpg",
      description: "Bacon ipsum dolor amet kevin spare ribs filet mignon meatloaf, short ribs brisket doner hamburger andouille turducken alcatra pork loin ground round. Jerky drumstick shank cow, turkey kielbasa salami turducken pork belly tongue. Landjaeger picanha pancetta jerky bacon brisket pork belly. Pork pork loin corned beef salami beef kielbasa alcatra strip steak. Shank burgdoggen shoulder, rump fatback shankle tenderloin porchetta kielbasa pork chop capicola doner boudin short ribs pig. Picanha sirloin venison, salami pastrami pancetta frankfurter flank meatloaf rump.",
      author: {}
   },
   {
      name: "Reimers",
      image: "http://www.stavislost.com/images/photography/2016/54cacb9abc715.jpg",
      description: "Bacon ipsum dolor amet kevin spare ribs filet mignon meatloaf, short ribs brisket doner hamburger andouille turducken alcatra pork loin ground round. Jerky drumstick shank cow, turkey kielbasa salami turducken pork belly tongue. Landjaeger picanha pancetta jerky bacon brisket pork belly. Pork pork loin corned beef salami beef kielbasa alcatra strip steak. Shank burgdoggen shoulder, rump fatback shankle tenderloin porchetta kielbasa pork chop capicola doner boudin short ribs pig. Picanha sirloin venison, salami pastrami pancetta frankfurter flank meatloaf rump.",
      author: {}
   },
   {
      name: "Hamilton Pool",
      image: "https://static.squarespace.com/static/547c911ee4b010fe66bcdd43/547c920ae4b0c94523f30326/547c920be4b0c94523f30b33/1343830173347/1000w/14990144-19675455-thumbnail.jpg",
      description: "Bacon ipsum dolor amet kevin spare ribs filet mignon meatloaf, short ribs brisket doner hamburger andouille turducken alcatra pork loin ground round. Jerky drumstick shank cow, turkey kielbasa salami turducken pork belly tongue. Landjaeger picanha pancetta jerky bacon brisket pork belly. Pork pork loin corned beef salami beef kielbasa alcatra strip steak. Shank burgdoggen shoulder, rump fatback shankle tenderloin porchetta kielbasa pork chop capicola doner boudin short ribs pig. Picanha sirloin venison, salami pastrami pancetta frankfurter flank meatloaf rump.",
      author: {}
   }
   ]

function seedDB() {
   var user = "";
   User.find({"username": "nick"}, (err, item) => {
      if (err) {
         console.log("error");
      } else {
         user = item[0];
         console.log(user);      
      }
   });
   
   Comment.remove({}, (err) => {
      if (err) {
         console.log(err);
      } else {
         console.log("removed comments!");
         Campground.remove({}, (err) => {
            if (err) {
               console.log(err);
            } else {
               console.log("removed campgrounds!");
               data.forEach((seed) => {
                  seed.author.id = user._id;
                  seed.author.username = user.username;
                  console.log(seed);
                  Campground.create(seed, (err, campground) => {
                     if (err) {
                        console.log(err);
                     } else {
                        console.log("added a campground");
                        // create a comment
                        Comment.create(
                           { 
                              text: "This is great, but I wish there was internet",
                              author: {
                                 id: user._id,
                                 username: user.username
                              }
                           }, (err, comment) => {
                              if (err) {
                                 console.log(err);
                              } else {
                                 comment.save();
                                 campground.comments.push(comment);
                                 campground.save();
                                 console.log("Created new comment");
                              }
                           }
                        )
                     }
                  });   
               });
            }
         });
      }
   });
   
}

module.exports = seedDB;