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
	tags: [String],
	created: {
		type: Date,
		default: Date.now
	},
	location: {
		type: {
			type: String,
			default: "Point"
		},
		coordinates: [{
			type: Number,
			required: "You must supply coordinates!"
		}],
		address: {
			type: String,
			required: "You must supply an address!"
		}
	},
	photo: String
});

// NOTE: this can't be an arrow function (needs to be a proper function) because we need the this pointer.
// NOTE: only needs to run this funciton when the name has been changed
storeSchema.pre("save", async function(next) {
	if (!this.isModified("name")) {
		next();
		return;
	}
	// TODO: make sure slugs are unique
	this.slug = slug(this.name);
	// find other stores that have a slug of wes, wes-1, wes-2
	const slugRegEx = new RegExp(`^(${this.slug})((-[0-9]*$)?)$`, 'i');
	const storesWithSlug = await (this.constructor).find({ slug: slugRegEx });
	if (storesWithSlug.length) {
		this.slug = `${this.slug}-${storesWithSlug.length + 1}`;
	}

	next();
});

// uss a proper function here so you can use the this pointer.  arrow function won't work
storeSchema.statics.getTagsList = function() {
	return this.aggregate([
		{ $unwind: "$tags" },
		{ $group: { _id: "$tags", count: { $sum: 1 }}},
		{ $sort: { count: -1 }}
	]);
}

module.exports = mongoose.model("Store", storeSchema);