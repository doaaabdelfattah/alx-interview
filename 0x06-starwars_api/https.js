const https = require("https");

// URL of the Star Wars API (Make sure this URL is correct)
const apiUrl = "https://swapi-api.alx-tools.com/api/people/1/";

https.get(apiUrl, (response) => {
  let data = '';

  // A chunk of data has been received.
  response.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  response.on('end', () => {
    // Check the content type to ensure it's JSON
    const contentType = response.headers['content-type'];

    if (contentType.includes('application/json')) {
      try {
        const json = JSON.parse(data);
        console.log(json);
      } catch (error) {
        console.error("Error parsing JSON:", error);
      }
    } else {
      console.error("Received non-JSON response:", data);
    }
  });
}).on("error", (err) => {
  console.error("Error: " + err.message);
});
