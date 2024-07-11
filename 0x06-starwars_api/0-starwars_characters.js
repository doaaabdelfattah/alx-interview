#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const getData = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(`Request failed: ${error.message}`);
        return;
      }
      const contentType = response.headers['content-type'];
      if (contentType && contentType.includes('application/json')) {
        try {
          const newData = JSON.parse(body).characters; // Array of character URLs
          // Using Promise.all to handle multiple asynchronous calls
          Promise.all(newData.map(characterUrl => {
            return new Promise((resolveCharacter, rejectCharacter) => {
              request(characterUrl, (errorCharacter, responseCharacter, bodyCharacter) => {
                if (errorCharacter) {
                  rejectCharacter(`Request failed for ${characterUrl}: ${errorCharacter.message}`);
                  return;
                }
                try {
                  const characterData = JSON.parse(bodyCharacter);
                  resolveCharacter(characterData.name); // Resolve with character name
                } catch (parseError) {
                  rejectCharacter(`Error parsing JSON for ${characterUrl}: ${parseError.message}`);
                }
              });
            });
          })).then(characters => {
            resolve(characters.join('\n')); // Join array into a single string with newline separators
          }).catch(error => {
            reject(`Error fetching character data: ${error}`);
          });
        } catch (error) {
          reject(`Error parsing JSON: ${error}`);
        }
      } else {
        reject("Received non-JSON response");
      }
    });
  });
};

getData(url)
  .then((data) => {
    console.log("Character Names:\n", data); // Print as a list of strings
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
  });
