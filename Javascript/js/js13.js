let element = document.createElement('li');
// let element = document.createElement('a');
console.log(element);
let text = document.createTextNode("akhil");
console.log(text);
element.appendChild(text);
console.log(element);
element.setAttribute("type", "square")
console.log(element);
let ele=document.getElementById("insert")
ele.innerHTML=element.outerHTML;
element.setAttribute("class", "childul")
console.log(element);

let desc = document.createElement('b')
desc.id = "quotes";
console.log(desc);
desc.className = "quotes";
console.log(desc);
let insertdesc = document.createTextNode("WE WILL BE SOON MOVING ON TO DJANGO REACT");
desc.appendChild(insertdesc)


let getIdname = document.getElementById('friends')
// getIdname.replaceWith(desc)
getIdname.appendChild(desc)
getIdname.removeAttribute("id")
getIdname.setAttribute('href', '//arkprocoder.tech')
getIdname.setAttribute('style','color:blue;')