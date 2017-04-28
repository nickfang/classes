// var request = require("request");
// request("http://www.google.com", (error, response, body) => {
//    if (!error && response.statusCode == 200) {
//       console.log(body)
//    }
// });

var request = require("request");
request("http://xkcd.com/1814/info.0.json", (error, response, body) => {
   if (!error && response.statusCode == 200) {
      var parsedData = JSON.parse(body);
      console.log(parsedData["alt"]);
   }
});
