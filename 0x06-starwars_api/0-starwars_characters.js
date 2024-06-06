#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];

const movieURL = `https://swapi.dev/api/films/${movieID}/`;

function fetchCharacters(movieURL) {
  return new Promise((resolve, reject) => {
    request(movieURL, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const filmData = JSON.parse(body);
        const charactersURLs = filmData.characters;
        resolve(charactersURLs);
      }
    });
  });
}

async function printCharacters(movieID) {
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
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData);
      }
    });
  });
}

printCharacters(movieID);
