const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const port = process.env.PORT || 3000;
const http = require('http').Server(app);
const io = require('socket.io')(http);

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

let currPh = 7;
let currTemp = 70;
let currMoisture = 50;

// Emit the updated data every second
setInterval(() => {
  currPh = updateValue(currPh, 0, 0.1, 0, 14);
  currTemp = updateValue(currTemp, 0, 1, -50, 50);
  currMoisture = updateValue(currMoisture, 0, 5, 0, 100);
  console.log('PH:', currPh, 'Temp:', currTemp, 'Moisture:', currMoisture);

  io.emit('data', { currPh, currTemp, currMoisture });
}, 100);

let deviceData = {};  // to store the form data

app.get('/index.html', (req, res) => {
  res.render('index', { title: 'Home' });
});

app.post('/submit', (req, res) => {
  deviceData = {
    deviceName: req.body.deviceName,
    deviceId: req.body.deviceId,
    phone: req.body.phone,
    highPH: req.body.highPH,
    lowPH: req.body.lowPH,
    highTemp: req.body.highTemp,
    lowTemp: req.body.lowTemp,
    highMoisture: req.body.highMoisture,
    lowMoisture: req.body.lowMoisture
  };

  res.redirect('/dashboard');  // redirect to the dashboard after receiving the form data
});

app.get('/dashboard', (req, res) => {
  res.render('dashboard', { 
    phData: currPh,
    tempData: currTemp,
    moistureData: currMoisture,
    deviceName: deviceData.deviceName,
    deviceId: deviceData.deviceId,
  });
});

// Function to update a value within a certain range
function updateValue(value, minChange, maxChange, minValue, maxValue) {
  const change = minChange + Math.random() * (maxChange - minChange);
  value += Math.random() < 0.5 ? -change : change;
  return Math.max(minValue, Math.min(maxValue, value));
}

http.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});