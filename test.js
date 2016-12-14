/**
 * Created by carlos.gonzalez on 13/12/16.
 */
fs = require('fs');
var http = require("https");
var options = {
    host: "api.projectoxford.ai",
    path: "/face/v1.0/detect",
    method: "POST",
    headers: {
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": "",
        "Content-Length": fs.readFileSync('sergio_fajardo_alcalde_medellin.jpg').length
    }
};
var req = http.request(options, function (res) {
    var responseString = "";

    res.on("data", function (data) {
        responseString += data;
        // save all the data from response
    });
    res.on("end", function () {
        console.log(responseString);
        // print to console when response ends
    });
});

fs.readFile('sergio_fajardo_alcalde_medellin.jpg',function (err, file) {
    req.write(file);
    req.end();
});
