var mongoose = require("mongoose");
mongoose.connect("mongodb://localhost/blog_demo_2");

var Post = require("./models/post");
var User = require("./models/user");

// // Post - title, content
// var postSchema = new mongoose.Schema({
//    title: String,
//    content: String
// });

// var Post = mongoose.model("Post", postSchema);

// // User - email name
// var userSchema = new mongoose.Schema({
//    email: String,
//    name:String,
//    posts: [
//       {
//          type: mongoose.Schema.Types.ObjectId,
//          ref: "Post"
//       }
//    ]
// });

// var User = mongoose.model("User", userSchema);

// User.create({
//    email: "bob@gmail.com",
//    name: "Bob Belcher"
// });

Post.create({
   title: "How to cook the best burger pt. 4",
   content: ";alskdf aslkdjfoiwenvlko nlvxiocjaew  sldkjfoiwnea"
   }, (err, post) => {
      if (err) {
         console.log(err);
      } else {
         User.findOne({email: "bob@gmail.com"}, (err, foundUser) => {
            if (err) {
               console.log(err);
            } else {
               foundUser.posts.push(post);
               foundUser.save((err, data) => {
                  if (err) {
                     console.log(err);
                  } else {
                     console.log(data);
                  }
               });
            }
         });
      }
});

// User.findOne({email: "bob@gmail.com"}).populate("posts").exec((err, user) => {
//    if (err) {
//       console.log(err);
//    } else {
//       console.log(user);
//    }
// });