const mongoose = require("mongoose");
mongoose.Promise = global.Promise;
const slug = require("slugs");

// NOTE: good to do data normalization as close to the model
// NOTE: strict schema
const storeSchema = new mongoose.Schema({
	name: {
		type: String,
		trim: true,
		required: 'Please enter a store name!'
	},
	slug: String,
	description: {
		type: String,
		trim: true
	},
	tags: [String]
});

// NOTE: this can't be an arrow function (needs to be a proper function) because we need the this pointer.
// NOTE: only needs to run this funciton when the name has been changed
storeSchema.pre("save", function(next) {
	if (!this.isModified("name")) {
		next();
		return;
	}
	// TODO: name sure slugs are unique
	this.slug = slug(this.name);
	next();
})

module.exports = mongoose.model("Store", storeSchema);