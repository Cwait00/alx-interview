#!/usr/bin/node

const request = require('request');

// Get movie ID from command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// API endpoint for the specified movie
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

const fetchCharacter = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
};

request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  for (const character of characters) {
    try {
      const name = await fetchCharacter(character);
      console.log(name);
    } catch (error) {
      console.error(error);
    }
  }
});
