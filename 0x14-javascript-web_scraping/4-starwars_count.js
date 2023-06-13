#!/usr/bin/node

const query = require('request');

query(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const instance = JSON.parse(body).results.filter((elem) => {
    return elem.characters.filter((url) => { return url.includes('18'); }).length;
  }).length;
  console.log(instance);
});
