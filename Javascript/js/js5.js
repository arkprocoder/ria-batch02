console.log("js-5");
console.log(document);

const name="Anees";
const greet="Good Evening"
let html;

html="<h1> Hello This is JS"+"<p>This is ria </p>"
// document.write(html)
console.log(html.length);
console.log(html.toLocaleLowerCase());
console.log(html.toUpperCase());
console.log(html.charAt(5));
console.log(html.endsWith('>'));
console.log(html.startsWith('>'));
console.log(html.lastIndexOf('i'));
console.log(html.includes('This'));
console.log(html.substring(5,10));
console.log(html.split(' '));
console.log(html.replace('ria','javascript'));
console.log(html.trim());
let text1 = "sea";
let text2 = "food";
let result = text1.concat(" ",text2);
console.log(result);


let myfriends=["Rohan","Rakshith","harshith","amrutha"]
let mydata=`
<h1>My friends using Template literals </h1>
<p> ${myfriends} </p>
`

console.log(mydata);

document.body.innerHTML+=mydata;