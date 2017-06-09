const mongoose = require("mongoose");
// NOTE: we're already imported the store schema.  It's a singleton so access it from mongoose
const Store = mongoose.model("Store");
// NOTE: used to send files in multiple parts and resize it
const multer = require("multer");
const jimp = require("jimp");
const uuid = require("uuid");

const multerOptions = {
	storage: multer.memoryStorage(),
	fileFilter: (req, file, next) => {
		const isPhoto = file.mimetype.startsWith("image/");
		if (isPhoto) {
			// NOTE: first value is the error
			next(null, true);
		} else {
			next({ message: "That filetype isn\'t allowed!" }, false);
		}
	}
};

exports.homePage = (req, res) => {
	res.render("index");
};

exports.addStore = (req, res) => {
	res.render("editStore", { title: "Add Store" });
};

exports.upload = multer(multerOptions).single("photo");

exports.resize = async (req, res, next) => {
	// check if there is no new file to resize
	if (!req.file) {
		next(); // skip to the next middleware
		return;
	}
	const extension = req.file.mimetype.split("/")[1];
	req.body.photo = `${uuid.v4()}.${extension}`;
	// now we resize
	const photo = await jimp.read(req.file.buffer);
	await photo.resize(800, jimp.AUTO);
	await photo.write(`./public/uploads/${req.body.photo}`);
	// once we have written the photo to our filesystem, keep going!
	next();
}

exports.createStore = async (req, res) => {
	// NOTE: check if the data being passed back is good.
	// req.body.location.coordinates[0] = Number(req.body.location.coordinates[0]);
	// req.body.location.coordinates[1] = Number(req.body.location.coordinates[1]);
	// res.json(req.body);
	// console.log("createStore:", req.body);
	const store = await (new Store(req.body)).save();
	// NOTE: how to add new elemnts to mongodb
	// store.age = 10
	// store.location = "corner of elm and late"
	// store.save()
	// NOTE: use promises to avoid callback hell.  This was initialized in the app.js
	// NOTE: await will not move on until the save has happened
	// NOTE: to catch an error with async await, you have to wrap your code with a try...  or use composition.  wrap createStore that handles the error.  catchErrors in errorHandlers handles this.
	// NOTE: app.js will pass from "/" to the error handlers and stop on the one that works
	req.flash("success", `Successfully Created ${store.name}.  Care to leave a review?`);
	res.redirect(`/store/${store.slug}`);

}

exports.getStores = async (req, res) => {
	const stores = await Store.find();
	res.render("stores", {title: 'Stores', stores});
}

exports.editStore = async (req, res) => {
	// find the store given the ID
	const store = await Store.findOne({ _id: req.params.id });
	// console.log("editStore:",store);
	// TODO: confirm they are the owner of the store
	// Render out the edit form so the user can update
	// NOTE: in ES6, if the key and value are the same, you just have to write it once.
	res.render("editStore", { title: `Edit ${store.name}`, store});
}

exports.updateStore = async(req, res) => {
	// set  the location data to be a point
	req.body.location.type = "Point";
	// find and update the store

	const store = await Store.findOneAndUpdate({ _id: req.params.id}, req.body, {
		new: true, // return the new store instead of the old one
		runValidators: true
	}).exec();
	// console.log("updateStore", req.body);
	req.flash("success", `Successfully updated <strong>${store.name}</strong>. <a href="/store/${store.slug}">View Store </a>`);
	res.redirect(`/stores/${store._id}/edit`);
	// redirect them to the store and tell them it worked
};

exports.getStoreBySlug = async (req, res, next) => {
	const store = await Store.findOne({ slug: req.params.slug });
	if (!store) return next();
	res.render("store", { store, title: store.name });
}