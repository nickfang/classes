var fake = require("faker");

function listProducts() {
    var welcome = "WELCOME TO MY SHOP!";
    var borders = "===================";
    console.log(borders);
    console.log(welcome);
    console.log(borders);
    for (var i = 0; i < 10; i++) {
        console.log(fake.fake("{{internet.domainName}} - {{internet.ip}}"));
        // console.log(fake.internet.domainName(), fake.internet.ip());
    }
}

listProducts();