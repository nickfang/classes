const express = require('express');
const router = express.Router();
const storeController = require('../controllers/storeController');

const {catchErrors} = require("../handlers/errorHandlers");

router.get('/', storeController.homePage);
router.get("/add", storeController.addStore);
// NOTE: passing storeController.createStore into catchError and passes back a catch
router.post("/add", catchErrors(storeController.createStore));

module.exports = router;
