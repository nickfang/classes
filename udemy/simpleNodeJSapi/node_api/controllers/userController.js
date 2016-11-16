var helpers = require('../config/helperFunctions.js');
var userModel = require('../models/userModel.js');

module.exports = function(server) {
	server.get("/", function(req, res, next) {
		userModel.find({}, function (err, users) {
			helpers.success(res, next, users);
		})
	});

	server.get("/user/:id", function(req, res, next) {
		req.assert('id', 'ID is required and must be numeric').notEmpty();
		var errors = req.validationErrors();
		if (errors) {
			helpers.failure(res, next, errors[0], 400);
		}
		userModel.findOne({ _id: req.params.id }, function(err, user) {
			if (err) {
				helpers.failure(res, next, 'Error fetching the user from the database', 500)
			}
			if (user == null) {
				helpers.failure(res, next, 'The specified user could not be found', 404);
			}
			helpers.success(res, next, user);
		});
	});

	server.post("/user", function(req, res, next) {
		req.assert('first_name', 'First name is required').notEmpty();
		req.assert('last_name', 'Last name is required').notEmpty();
		req.assert('email_address', 'Email address is required and must be a valid email').notEmpty().isEmail();
		req.assert('career', 'Career must be either student, teacher, or professor').isIn(['student', 'teacher', 'professor']);
		var errors = req.validationErrors();
		if (errors) {
			helpers.failure(res, next, errors, 400);
		}
		else {
			var user = new userModel();
			user.first_name = req.params.first_name;
			user.last_name = req.params.last_name;
			user.email_address = req.params.email_address;
			user.career = req.params.career;
			user.save(function(err) 	{
				if (err) {
					helpers.failure(res, next, errors, 500);
				}
			})
			helpers.success(res, next, user);
		}
	});

	server.put("/user/:id", function(req, res, next) {
		req.assert('id', 'ID is required and must be numeric').notEmpty();
		var errors = req.validationErrors();
		if (errors) {
			helpers.failure(res, next, errors[0], 400);
		}
		userModel.findOne({ _id: req.params.id }, function(err, user) {
			if (err) {
				helpers.failure(res, next, 'Something went wrong when fetching the user from the database', 500)
			}
			if (user == null) {
				helpers.failure(res, next, 'The specified user could not be found', 404);
			}
			var updates = req.params;
			delete updates.id;
			for (var field in updates) {
				user[field] = updates[field];
			}
			user.save(function (err) {
				if (err) {
					helpers.failure(res, next, 'Error saving user to the database', 500)
				}
			})
			helpers.success(res, next, user);
		});
	});

	server.del("/user/:id", function(req, res, next) {					// get is for retreiving info about user
		req.assert('id', 'ID is required and must be numeric').notEmpty();
		var errors = req.validationErrors();
		if (errors) {
			helpers.failure(res, next, errors[0], 400);
		}
		userModel.findOne({ _id: req.params.id }, function(err, user) {
			if (err) {
				helpers.failure(res, next, 'Something went wrong when fetching the user from the database', 500)
			}
			if (user == null) {
				helpers.failure(res, next, 'The specified user could not be found', 404);
			}
			user.remove(function (err) {
				if (err) {
					helpers.failure(res, next, 'Error removing user from the database', 500)
				}
			})
			helpers.success(res, next, user);
		});
	});
}