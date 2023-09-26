#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

function movieTitle (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let jsonDict = JSON.parse(body);
      console.log(jsonDict.title);
    }
  });
}
movieTitle(url);