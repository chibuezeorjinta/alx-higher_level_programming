#!/usr/bin/node

const query = require('request');

query('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(body).title);
});
