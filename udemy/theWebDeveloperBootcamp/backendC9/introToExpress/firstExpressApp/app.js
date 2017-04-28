var express = require("express");
var app = express();

// "/" => "Hi there!"
app.get("/", (req, res) => {
    res.send("Hi there!");
});


// "/bye" => "Goodbye!"
app.get("/bye", (req, res) => {
   res.send("Goodbye!"); 
});

// "/dog" => "MEOW!"
app.get("/dog", (req, res) => {
   res.send("MEOW!"); 
});

app.get("/r/:subredditName", (req, res) => {
    var subreddit = req.params.subredditName.toUpperCase();
    res.send(`Welcome to the ${subreddit} subreddit!`);
});

app.get("*", (req, res) => {
    res.send("You are a Star!!");
});


app.listen(process.env.PORT, process.env.IP, () => {
    console.log("server has started!!");
});