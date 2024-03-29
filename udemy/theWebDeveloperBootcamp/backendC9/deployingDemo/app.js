var app = require("express")();

app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.render("home"); 
});

app.get("/about", (req, res) => {
   res.render("about");
});

app.listen(process.env.PORT, process.env.IP);