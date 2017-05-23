const mongoose = require("mongoose");
// NOTE: we're already imported the store schema.  It's a singleton so access it from mongoose
const Store = mongoose.model("Store");

exports.homePage = (req, res) => {
	console.log(req.name);
	res.render("index");
};

exports.addStore = (req, res) => {
	res.render("editStore", { title: "Add Store" });
};

exports.createStore = async (req, res) => {
	// NOTE: check if the data being passed back is good.
	// res.json(req.body);
	const store = new Store(req.body);
	// NOTE: how to add new elemnts to mongodb
	// store.age = 10
	// store.location = "corner of elm and late"
	// store.save()
	// NOTE: use promises to avoid callback hell.  This was initialized in the app.js
	// NOTE: await will not move on until the save has happened
	// NOTE: to catch an error with async await, you have to wrap your code with a try...  or use composition.  wrap createStore that handles the error.  catchErrors in errorHandlers handles this.
	// NOTE: app.js will pass from "/" to the error handlers and stop on the one that works
	await store.save();
	res.redirect("/");
}