setTimeout(myFunction, 10000);

setTimeout(greet,5000);


function run(){
    console.log("i am running");
}

function myFunction() {
  document.getElementById("demo").innerHTML = "I love javascript !!";
}

function greet(){
    document.getElementById("greet").innerHTML = "Good morning !!";
}

run()