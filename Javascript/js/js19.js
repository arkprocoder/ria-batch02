// let myPromise = new Promise(function(myResolve, myReject) {
//     // "Producing Code" (May take some time)
    
//       myResolve(); // when successful
//       myReject();  // when error
//     });
    
//     // "Consuming Code" (Must wait for a fulfilled Promise)
//     myPromise.then(
//       function(value) { /* code if successful */ },
//       function(error) { /* code if some error */ }
//     );


function myDisplayer(some) {
    document.getElementById("demo").innerHTML = some;
  }
  
let myPromise = new Promise(function(myResolve, myReject) {
    let x = 10;
  
  // The producing code (this may take some time)
  
    if (x == 0) {
      myResolve("OK");
    } else {
      myReject("Error");
    }
  });
  
myPromise.then(
    function(value) {myDisplayer(value);},
    function(error) {myDisplayer(error);}
  );


let myPromise1 = new Promise(function(myResolve, myReject) {
    setTimeout(function() { myResolve("I love python !!"); })
    setTimeout(function() { myReject("I love java !!"); }, 3000);
});
  
myPromise1.then(
    //resolved
    function(value) {
    document.getElementById("demo1").innerHTML = value;
  },
  
    function(value) {
    document.getElementById("demo1").innerHTML = value;
  },
  
  
  );
  
  