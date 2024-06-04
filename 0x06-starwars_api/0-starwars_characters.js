#!/usr/bin/node

const request = require('request');

// Extracting movie ID from command line arguments
const movieID = process.argv[2];

// API endpoint for fetching movie data
const movieURL = `https://swapi.dev/api/films/${movieID}/`;

// Function to fetch character data for a given movie
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

// Function to fetch and display character names
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

// Function to fetch character data from a given character URL
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

// Calling the function to print character names
printCharacters(movieID);
