#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    // Fetching all character names
    characters.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
          return;
        }

        if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.error(`Error: Unable to fetch movie with ID ${movieId}`);
  }
});
