const express = require('express');
const app = express();
const PORT = 3001;
const mongo = require('mongodb');
const MongoClient = mongo.MongoClient;
// insert password
var url = "mongodb+srv://qhacks:<PASSWORD>@cluster0-brdw1.mongodb.net/test?retryWrites=true"
var db;

MongoClient.connect(url, function(err, client) {
  if (err) throw err;
  db = client.db('qhacks')
});

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/screenshots/:id', async (req, res) => {
  try {
    var screenshots =[]
    const collection = await db.collection('screenshots')
    let arr = await collection.find({
      youtube_id: req.params.id
    }).toArray()
    arr.forEach(el => {
      screenshots.push(el.file)
    })
    res.send(screenshots)
  } catch (error) {
    console.log(error)
  }
})

app.get('/timestamps/:id/:keyword', async (req, res) => {
  try {
    var timestamps = []
    const collection = await db.collection('timestamps')
    let arr = await collection.find({
      youtube_id: req.params.id,
      keyword: req.params.keyword
    }).toArray()
    arr.forEach(el => {
      timestamps.push(parseInt(el.secs))
    });
    res.send(timestamps)
  } catch (error) {
    console.log(error)
  }
})

app.get('/transcripts/:id', async (req, res) => {
  try {
    const collection = db.collection('transcripts')
    let jsonData = await collection.find({
      youtube_id: req.params.id
    }).toArray();
    res.send(JSON.stringify(jsonData[0].transcript))
  } catch (error) {
    console.log(error)
  }
})

app.listen(PORT, () => {
  console.log('Listening on port', PORT);
})
