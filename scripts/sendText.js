//MAIN function to reach out to the server
function sendText(text){
    //First, we define the value from the text, to allow better usage of variables
    var value = text;
    //console.log("value",value);
    //console.log('textContent ',document.getElementById("input").textContent);

    var languageSelected = document.getElementById("languageSelection").value;
    var recordedCursorPosition = getCurrentCursorPosition('input');

    console.log('cursor position:',getCurrentCursorPosition('input'));

    var baseUrlEndpoint = "http://localhost:5000/process?"

    //Third, we use the fetch method to call the localhost asynchronously (Synchronously was not recommended)
    //This is where we get the results from the index.js file
    //fetch("http://localhost:8080/spellCheck?lng="+languageSelected+"&text="+value, {
    fetch( baseUrlEndpoint+ "lng=" + languageSelected+"&phrase="+value, {
        method: 'GET'
    }).then(prior =>  prior.json()).then(
        final => {
            //At this point the index.js file responded and we have a response body
            console.log(final);

            //We get our response in a variable
            var response = final;
              
            //get the length to the suggestions array returned
            var suggestionsLength =  response.suggestions.length;

            //created a new array and populated it with the list of incorrect words
            var incorrectWords = [];
            for(var x= 0; x<suggestionsLength; x++){
                incorrectWords.push(response.suggestions[x].word);
            }


            var suggestions = response.suggestions;
            
            
            console.log('incorrectWords: ',incorrectWords);
            //trigger the function to get the red lines show up or disappear
            getRedLines(incorrectWords, recordedCursorPosition);

            //console.log('suggestions',suggestions);

            for(let z = 0; z < suggestionsLength; z++){ 
                
                let originalWord = suggestions[z].word; 
                let positionInArray = z; 
                //console.log(originalWord);          
                let suggestionsForWordOne = suggestions[z].suggestions;
                //let wordElement = document.getElementById(suggestions[z].word);
                let wordElement = document.getElementById(z);                    
                if(wordElement){
                    wordElement.onmousedown = function(event) {
                        let suggestionsForWord = suggestions[z].suggestions                            
                        if (event.button == 2) {                            
                            $('#contextMenu').append('<ul id="wordList"></ul>');   
                            if(suggestionsForWord.length){
                                for(let u = 0; u < suggestionsForWord.length; u++){
                                    let individualSuggestion = suggestionsForWord[u];
                                    $('#wordList').append("<li onclick=\"changeWord('"+positionInArray+"','"+individualSuggestion+"')\">"+individualSuggestion+'</li>');
                                } 
                            } else {
                                $('#wordList').append("<li>No suggestions</li>")
                            }                                                                                                                     
                        }
                    }
                }
                
                
            }

        
         }
    ).catch(function(error){
        //TODO: work on an error response
    })

    
    
    
}