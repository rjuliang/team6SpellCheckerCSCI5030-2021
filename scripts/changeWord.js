//Changes the word when clicked suggestion on right click menu
function changeWord (wordMisspelled, correction){
            
    let wordLocation = document.getElementById(wordMisspelled)
    let originalContent = wordLocation.textContent;
    let trimmedtext = originalContent.trim();
    let lastCharacter = trimmedtext.slice(-1);
    let characters = /^[a-zA-Z0-9]+$/;
    let addedCharacter = !characters.test(lastCharacter) ? lastCharacter : "";

    document.getElementById(wordMisspelled).textContent = correction + addedCharacter +" ";
    $('#'+wordMisspelled).removeClass('red_line').addClass('other');
    $('#'+wordMisspelled).focusEnd();
}