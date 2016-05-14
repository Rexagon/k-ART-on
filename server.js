var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');

// Configure app
var app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, "views"));

// Use middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'views')));

// Define routes
app.use('/', require('./routes/index'));

app.listen(process.env.PORT || 1337, function() {
  console.log('Server is running');
});
