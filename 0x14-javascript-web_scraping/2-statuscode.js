#!/usr/bin/node

const response = require('request');

response(process.argv[2], function (err, out) {
  if (err) {
    console.error(err);
  }
  console.log('code:', out && out.statusCode);
});
