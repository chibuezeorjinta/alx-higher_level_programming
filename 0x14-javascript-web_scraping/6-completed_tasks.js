#!/usr/bin/node

const query = require('request');

query(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const dict = JSON.parse(body).reduce((key, task) => {
    if (!key[task.userId]) {
      if (task.completed) {
        key[task.userId] = 1;
      }
    } else {
      if (task.completed) {
        key[task.userId] += 1;
      }
    }
    return key;
  }, {});
  console.log(dict);
});
