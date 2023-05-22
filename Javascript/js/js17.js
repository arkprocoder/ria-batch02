console.log("call backs")

// function myDisplayer(some) {
//     document.getElementById("demo").innerHTML = some;
//   }
  
// function myCalculator(num1, num2) {
//     let sum = num1 + num2;
//     return sum;
//   }
  
// let result = myCalculator(5, 5);
// myDisplayer(result);

function myDisplayer(some) {
    document.getElementById("demo").innerHTML = some;
  }
  
function myCalculator(num1, num2, myDisplayer) {
    let some = num1 + num2;
    myDisplayer(some);
  }
  
myCalculator(15, 5, myDisplayer);


// Create an Array
const myNumbers = [4, 1, -20, -7, 5, 9, -6];

// Call removeNeg with a callback
const posNumbers = removeNeg(myNumbers, (x) => x >= 0);

// Display Result
document.getElementById("demo").innerHTML = posNumbers;

// Keep only positive numbers
function removeNeg(numbers, anything) {
  const myArray = [];
  for (const x of numbers) {
    if (anything(x)) {
      myArray.push(x);
    }
  }
  return myArray;
}