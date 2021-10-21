//function (fn) to underline words
function getRedLines (incorrectWords, cursorPosition){
    console.log('cursorPosition',cursorPosition);
    var newHTML = "";
    $('#input').text().replace(/[\s]+/g, " ").trim().split(" ").forEach(function(val, idx){
        // If word is statement

        //console.log('val', val);//.replace(/[^\w\s]/gi, '')

        let newVal = val.replace(/[^\w\s]/gi, '')

        if (incorrectWords.indexOf(val.trim()) > -1)
            newHTML += "<span id='"+incorrectWords.indexOf(val.trim())+"'class='red_line'>" + val + "&nbsp;</span>";
        else
            newHTML += ""+val+" "; 
    });
    //console.log('newHTML',newHTML);

    //var insertedBreaks = newHTML.replace("ENTERPAR5", "<br>");
    $('#input').html(newHTML);
    $('#input').focusEnd();
    //setCurrentCursorPosition(cursorPosition);
    //console.log(getCurrentCursorPosition('input'));
}