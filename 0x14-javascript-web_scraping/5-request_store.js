#!/usr/bin/node

const query = require('request');
const file = require('fs');

query(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  try {
    file.writeFile(process.argv[3], body, 'utf8', function (err, result) { if (err) console.log(err); });
  } catch (err) {
    console.log(err);
  }
});

