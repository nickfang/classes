var restify = require('restify');
var restifyValidator = require('restify-validator');
var mongoose = require('mongoose');
var server = restify.createServer();

var setupController = require("./controllers/setupController.js");
var userController = require('./controllers/userController.js');
var config = require('./config/dbConnections.js');

mongoose.connect(config.getMongoConnection());
setupController(server, restify, restifyValidator);
userController(server);

server.listen(8080, function() {
  console.log('%s listening at %s', server.name, server.url);
});