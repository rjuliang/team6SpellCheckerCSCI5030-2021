
const express = require("express");
const Typo = require("typo-js");
const app = express();

let cors = require('cors')
app.use(cors())


//Separate words into an array
function separate(str) {
  //let myRegex = /[a-z0-9']+/gi;
  let myRegex = /\s/;
  //let words = str.match(myRegex);
  let words = str.split(myRegex);
  return words;
}

//Runs a check into an array of words
function spellCheck(phrase, lng){

  //Separate words into an array
  let arrayPhrase = separate(phrase); 
  //console.log(arrayPhrase);
  // calls the dictionary from the typo-js library
  let dictionary = new Typo(lng);

  //initialize arrays
  let misspelledWords = [];
  let suggestions = [];
  let numberRegex = /^\d*$/;
  //If arrayPhrase exists and is longer than 0, it runs a for loop to check for every word and see if each individual one is correct
  if(arrayPhrase && arrayPhrase.length > 0){
    for(let x = 0; x<arrayPhrase.length; x++){
      let word = arrayPhrase[x].trim();
      if(word != null && word != ""){
        let lastCharacter = word.slice(-1);
        let characters = /^[a-zA-Z0-9À-ÿ]+$/;
        let wordWithoutLastCharacter = word.replace(/[{()}]/g, '');
        //console.log(word);
        word = characters.test(lastCharacter) ? word: word.slice(0,-1);
        let wordToCheck = word.replace(/[{()}]/g, '');
        let is_spelled_correctly = dictionary.check(wordToCheck);
        let isNumber = numberRegex.test(wordToCheck);
        if(!is_spelled_correctly && !isNumber){
          //If the word is incorrect, we push it into the misspelledWords array
          misspelledWords.push(word);

          //If the word is incorrect, we request for suggestions and assign it into an array
          let array_of_suggestions = dictionary.suggest(word);
          suggestions.push({
            word: wordWithoutLastCharacter,
            suggestions: array_of_suggestions
          })
        } 
      }
      
    
    }
  }
  

  return suggestions;
}


//HERE is where the API receives the information from the /spellCheck path
app.get('/spellCheck', (req, res) => {
  
  //Assign the text to a constant
  const phrase = req.query.text;
  const lng = req.query.lng;
  console.log('Checking on:', lng);
  console.log('Server phrase received:',phrase);

  //Reach out to the spellCheck function for an array of suggestions
  let suggestions = spellCheck(phrase, lng);

  //We respond with an object with the original phrase and the suggestions array for individual words
  res.json({phrase: phrase, suggestions});
});

const port = 8080;

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
  console.log(`Open index.thml file`);
});