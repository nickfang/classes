var express = require("express");
var app = express();

function getErrorMessage() {
    return "Sorry, page not found... What are you doing with your life?";
}

app.get("/", (req, res) => {
   res.send("Hi there, welcome to my assignment!"); 
});

app.get("/speak/:animal", (req, res) => {
    var sounds = {
        pig: "Oink",
        cow: "Moo",
        dog: "Woof Woof!",
        cat: "Meow!"
    }
    
    var animal = req.params.animal.toLowerCase();
    var sound = sounds[animal];
    if (sound) {
        res.send(`The ${animal} says '${sound}'"`);
    } else {
        res.send(getErrorMessage());
    }
});

app.get("/repeat/:text/:num", (req, res) => {
   var str = "";
   for (var i = 0; i < req.params.num; i++ ) {
       str = str.concat(`${req.params.text} `);
   } 
   res.send(str);
});

app.get("*", (req, res) => {
    res.send(getErrorMessage());
});

app.listen(process.env.PORT, process.env.IP, () => {
    console.log("server has started!!");
});