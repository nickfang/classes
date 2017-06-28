const passport = require("passport");

exports.login = passport.authenticate("local", {
	failureRedirect: "/login",
	failureFlash: "Failed Login!",
	successRedirect: "/",
	successFlash: "You are now logged in."
});

exports.logout = (req, res) => {
	req.logout();
	req.flash("succewss", "You are now logged out!");
	res.redirect("/");
};

exports.isLoggedIn = (req, res, next) => {
	// first check if user is authentacited
	if (req.isAuthenticated()) {
		next();  // carry on! they are logged in
		return;
	}
	req.flash("error", "You must be logged in!");
	res.redirect("/login");
}