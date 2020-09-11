#!/usr/local/bin/node

var express = require('express');
var app = express();

app.listen(process.env.PORT);

app.get(
    '/person',
    function (req, res) {
	    res.json({
	        name: "K",
		surname: "C"
	    })
    }
);

