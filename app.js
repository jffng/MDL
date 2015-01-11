var express = require('express');
var app = express();
var http = require('http').Server(app);
var bodyParser = require('body-parser');
var exec = require('child_process').exec;

app.use("/", express.static(__dirname + "/public"));
app.use( bodyParser.json() );
app.use( bodyParser.urlencoded({
	extended: true
}));

app.get('/exercise1', function(req,res){
	res.sendFile(__dirname + '/public/exercise1.html');
});

app.get('/validate', function (req,res) {
	var sh = "python balance.py " + JSON.stringify(req.query.expr);
	var program;
	exec(sh, function(error, stdout, stderr){
		// console.log(stdout);
		program = stdout;
		res.jsonp({ expr: program});
	});
});

app.listen(3000, '127.0.0.1');

console.log('listening on port 3000')

