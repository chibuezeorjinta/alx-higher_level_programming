#!/usr/bin/node

const file = require('fs');

file.readFile(process.argv[2], 'utf-8', function (err, out) {
  if (err) {
    console.log(err);
  } else {
    console.log(out);
  }
});
