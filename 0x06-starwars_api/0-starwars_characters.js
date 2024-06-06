#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const baseURL = 'https://swapi.dev/api/films/';

function fetchCharacters(movieURL) {
  return new Promise((resolve, reject) => {
    request(movieURL, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch data: ${response.statusCode}`));
      } else {
        const filmData = JSON.parse(body);
        const charactersURLs = filmData.characters;
        resolve(charactersURLs);
      }
    });
  });
}

async function printCharacters(movieID) {
  const movieURL = `${baseURL}${movieID}/`;

  try {
    const charactersURLs = await fetchCharacters(movieURL);
    for (const characterURL of charactersURLs) {
      const characterData = await fetchCharacter(characterURL);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

function fetchCharacter(characterURL) {
  return new Promise((resolve, reject) => {
    request(characterURL, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch data: ${response.statusCode}`));
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData);
      }
    });
  });
}

printCharacters(movieID);
