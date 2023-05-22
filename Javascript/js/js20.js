/*
function myDisplayer(some) {
    console.log("i am async resolved function");
    document.getElementById("demo").innerHTML = some;
  }

async function  myFunction() {
    console.log("i am async function");
    return "Hello";

  }
  myFunction().then(
    function(value) {myDisplayer(value);},
    function(error) {myDisplayer(error);}
  );


console.log("i am async outside function");
*/


async function myDisplay() {
    let myPromise = new Promise(function(resolve) {
      setTimeout(function() {resolve("I love c !!");}, 3000);
    });
    document.getElementById("demo").innerHTML = await myPromise;
    console.log("i have complted the resolved state");
  }
  
myDisplay();