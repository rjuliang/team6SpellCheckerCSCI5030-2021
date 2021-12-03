//Triggering the word correction on spacekey press from the fkeyboard
document.body.onkeyup = function(e){
    if(e.keyCode == 32){
        //console.log('keyboard pressed', document.getElementById("input").innerText);

        // var htmlContent = document.getElementById("input").innerHTML;
        // var replacingBr = htmlContent.replace("<br>", " ENTERPAR5 ");
        // document.getElementById("input").innerHTML = replacingBr;
        var spellText = document.getElementById("input").innerText;
        //console.log('spellText',spellText);
        
        if(spellText != '' && spellText != null)
            sendText(spellText); // We trigger the function here
    }
}