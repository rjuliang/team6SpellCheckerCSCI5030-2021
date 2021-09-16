//import fs from 'fs';

const phrase = "This ia a mispelled wort";
const path = require("path");
const express = require("express");
const Typo = require("typo-js");
const bodyParser = require('body-parser');
const app = express();

var cors = require('cors')
app.use(cors())



function separate(str) {
  var myRegex = /[a-z0-9']+/gi;
  var words = str.match(myRegex);
  return words;
}

function spellCheck(phrase){
  var arrayPhrase = separate(phrase); 

  var dictionary = new Typo('en_US');

  var misspelledWords = [];
  var suggestions = [];

  for(var x = 0; x<arrayPhrase.length; x++){
    var word = arrayPhrase[x];
    var is_spelled_correctly = dictionary.check(word);
    if(!is_spelled_correctly){
      misspelledWords.push(word);
      var array_of_suggestions = dictionary.suggest(word);
      suggestions.push({
        word: word,
        suggestions: array_of_suggestions
      })
    }
  
  }

  return suggestions;
}

app.get('/check', (req, res) => {
  const phrase = req.query.spellText;
  console.log(phrase);
  var h = spellCheck(phrase);
  res.json({phrase: phrase, suggestions: h});
});

const port = 8080;

app.listen(port, () => {
  console.log(`Server running on port${port}`);
  // console.log('Words: ',arrayPhrase);
  // console.log('mispelled words: ',misspelledWords);
  // console.log('Suggestions: ',suggestions);
});


// app.get("/",function(request,response){
// response.send("Hello World!")
// })
// app.listen(10000, function () {
// console.log("Started application on port %d", 10000);
// //console.log(isRight);
// //console.log('is_spelled_correctly: ',is_spelled_correctly);
// //console.log('array_of_suggestions: ',array_of_suggestions);
// console.log('Words: ',arrayPhrase);
// console.log('mispelled words: ',misspelledWords);
// console.log('Suggestions: ',suggestions);
// });


// const fs  = require('fs');


// var en = require('dictionary-en');

// en(function (err, result) {
//   console.log(err || result)
// })

// var path = require('path');
// var base = require.resolve('dictionary-en');

// var Spellchecker = require("hunspell-spellchecker");
 
// var spellchecker = new Spellchecker();

// var DICT = spellchecker.parse({
//     aff: fs.readFileSync("./dictionaries/en_US.aff"),
//     //aff: fs.readFileSync(path.join(base, 'index.aff'), 'utf-8'),
//     dic: fs.readFileSync("./dictionaries/en_US.dic")
//     //dic:fs.readFileSync(path.join(base, 'index.dic'), 'utf-8')
// });

// spellchecker.use(DICT);

// var isRight = spellchecker.check("misspelled word");