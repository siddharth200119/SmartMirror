const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express();
const port = 5000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.post('/set-alarm', async (req, res) => {
  const { name, time } = req.body;

  // Update with the actual local API endpoint
  const alarmApiUrl = 'http://127.0.0.1:8080/api/set_alarm';

  try {
    // Format the time as HH:mm:ss
    const formattedTime = `${time}:00`;

    // Make a GET request to the local alarm API with parameters
    const response = await axios.get(alarmApiUrl, {
      params: {
        time: formattedTime,
        userName: name,
      },
    });

    console.log(response.data); // Log the API response
    res.send('Alarm set successfully!');
  } catch (error) {
    console.error('Error setting alarm:', error.message);
    res.status(500).send('Internal Server Error');
  }
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

