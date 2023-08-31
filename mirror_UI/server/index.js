const express = require("express");
const mongoose = require("mongoose");
const path = require('path');

const app = express()
app.set("view engine", "ejs");
app.use(express.static(__dirname + '/public'));
app.set('views', path.join(__dirname, '/views'));

