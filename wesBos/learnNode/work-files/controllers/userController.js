const mongoose = require("mongoose");
const User = mongoose.model("User");
const promisify = require("es6-promisify")

exports.loginForm = (req, res) => {
	res.render("login", { title: "login" })
};

exports.registerForm = (req, res) => {
	res.render("register", { title: "Register" })
};

exports.validateRegister = (req, res, next) => {
	// sanitizeBody from expressValidator;
	req.sanitizeBody("name");
	req.checkBody("name", "You must supply a name!").notEmpty();
	req.checkBody("email", "That email is not valid!").isEmail();
	req.sanitizeBody("email").normalizeEmail({
		remove_dots: false,
		remove_extension: false,
		gmail_remove_subaddress: false
	});
	req.checkBody("password", "Password cannot be blank!").notEmpty();
	req.checkBody("password-confirm", "Confirmed password cannot be blank!").notEmpty();
	req.checkBody("password-confirm", "Oops! Your passwords do not match!").equals(req.body.password);

	const errors = req.validationErrors();
	if (errors) {
		req.flash("error", errors.map(err => err.msg));
		res.render("register", { title: "Register", body: req.body, flashes: req.flash() })
		return; // stop the function from running
	}
	next(); // go to next middleware
};

exports.register = async (req, res, next) => {
	const user = new User({ email: req.body.email, name: req.body.name });
	const registerWithPromise = promisify(User.register, User);
	await registerWithPromise(user, req.body.password);
	// res.send("It works!!");
	next(); // pass to authController.login
	// the register function isn't a promise.
	// User.register(user, req.body.password, function(err, user) {

	// });
};

exports.account = (req, res) => {
	res.render("account", { title: "Edit your Account" });
}

exports.updateAccount = async (req, res) => {
	const updates = {
		name: req.body.name,
		email:req.body.email
	};
	const user = await User.findOneAndUpdate(
		{ _id: req.user._id },
		{ $set: updates },
		{ new: true, runValidators: true, context: "query" }
	);
	// res.json(user);
	req.flash("success", "Updated the profile!");
	res.redirect("back");
};