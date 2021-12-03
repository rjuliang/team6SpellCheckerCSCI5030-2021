/**
 * The following code was researched from https://www.geeksforgeeks.org/how-to-add-a-custom-right-click-menu-to-a-webpage/
 * Thanks to @devansh07 for writing the article that provided it.
*/
 document.onclick = hideMenu;
 document.oncontextmenu = rightClick;

 function hideMenu() {
     document.getElementById("contextMenu").style.display = "none"
     document.getElementById("contextMenu").innerHTML = "";
 }

 function rightClick(e) {
     e.preventDefault();

     if (document.getElementById(
         "contextMenu").style.display == "block")
         hideMenu();
     else {
         var menu = document
             .getElementById("contextMenu")
               
         menu.style.display = 'block';
         menu.style.left = e.pageX + "px";
         menu.style.top = e.pageY + "px";
     }
 }