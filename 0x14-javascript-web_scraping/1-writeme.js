#!/usr/bin/node

const file = require('fs');

try {
  file.writeFile(process.argv[2], process.argv[3], 'utf8', function (err, out) { if (err) console.log(err); });
} catch (err) {
  console.log(err);
}
