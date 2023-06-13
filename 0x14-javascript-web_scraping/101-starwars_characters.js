#!/usr/bin/node

const query = require('request');

function recursiveRequest (arr, i) {
  if (i === arr.length) {
    return;
  }
  query(arr[i], function (error, response, body) {
    if (error) {
      console.error(error);
    }
    console.log(JSON.parse(body).name);
    recursiveRequest(arr, i + 1);
  });
}

recursive('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const charac = JSON.parse(body).characters;
  recursiveRequest(charac, 0);
});
