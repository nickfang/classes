var express = require("express");
var app = express();

app.use(express.static("public"));
// this allows us to pass the file name with the ejs extension on the render function
app.set("view engine", "ejs")

app.get("/", (req, res) => {
    res.render("home");
});

app.get("/fallinlovewith/:thing", (req, res) => {
   var thing = req.params.thing;
   res.render("love", {thingVar: thing});
});     

app.get("/posts", (req, res) => {
    var posts = [
            {title: "Post1", author: "Susy1"},
            {title: "Post2", author: "Susy2"},
            {title: "Post3", author: "Susy3"}
    ];
    res.render("posts", {posts: posts});    
});



app.listen(process.env.PORT, process.env.IP, () => {
    console.log("Server is listening!!");
});
