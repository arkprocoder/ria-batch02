
function data() {
    return "Hello World!";
  }


hello = data()
// alert("ia m workimng");
console.log(hello);
  
const arrowFunction = (a,b) => {
    console.log("i am a arrow function")
    console.log("i a m workimng",a+b);
  }
arrowFunction(12,15)
arrowFunction()

// Arrow Function:
hello = () => {
    document.getElementById("demo").innerText += this;
  }
  
  // The window object calls the function:
//   window.addEventListener("load", hello);
  
  // A button object calls the function:
  document.getElementById("btn").addEventListener("click", hello);
