function changeLang() {
    var x="";
    x = document.getElementById("pageLanguage").value;
    
    if(x=="ga")
    {
        document.getElementById("title").innerHTML = "Seiceálaí Litrithe";
        document.getElementById("webLang").innerHTML = "Roghnaigh teanga leathanach gréasáin: ";
        document.getElementById("text").innerHTML = "Iontráil do théacs thíos: ";
        document.getElementById("textLang").innerHTML = "Roghnaigh teanga téacs: ";
        document.getElementById("button1").innerHTML = "Téacs Soiléir";
    }
    else       
    {
        document.getElementById("title").innerHTML = "Spell Checker";
        document.getElementById("webLang").innerHTML = "Select webpage language:  ";
        document.getElementById("text").innerHTML = "Enter your text below: ";
        document.getElementById("textLang").innerHTML = "Select text language: ";
        document.getElementById("button1").innerHTML = "Clear Text";
    }
}