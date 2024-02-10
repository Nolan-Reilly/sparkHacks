const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const port = process.env.PORT || 3000;

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

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
  let phData = [deviceData.lowPH, deviceData.highPH];
  let tempData = [deviceData.lowTemp, deviceData.highTemp];
  let moistureData = [deviceData.lowMoisture, deviceData.highMoisture];

  res.render('dashboard', { 
    phData: phData, tempData: tempData,
    moistureData: moistureData,
    deviceName: deviceData.deviceName,
    deviceId: deviceData.deviceId
  });

  
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});