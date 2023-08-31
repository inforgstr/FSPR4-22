// parentNode
// children

let anchor = document.querySelector("a");
// console.log(anchor.parentNode);
// anchor.parentNode.style.fontSize = "2em";
// console.log(anchor.children);
// anchor.children[0].style.display = "block";

let paragraph = document.querySelector("p");
paragraph.id = "info";
paragraph.innerHTML = "The text inside the paragraph";
paragraph.remove();

document.body.append(paragraph);

let paragraph_2 = document.querySelector("body>p");
// let paragraph_2 = document.querySelector("div>p");
// console.log(paragraph_2);
// document.querySelector("div").removeChild(paragraph_2);
// Removes only child that contains in parent element
document.body.removeChild(paragraph_2);

// to hide element we can use hidden property
document.getElementById("sign").hidden = true;
