console.log("functions");

// function greeting(){
//     console.log("good morning");
// }

// greeting();


function greeting(name,date){
    console.log("good morning",name,date);
}


let name="ria";
let date= new Date()
greeting(name,date);


function result(num1,num2){
     let res=num1+num2;
     console.log("addition is done");
     return res;
}


let data=result(15,25);
console.log("result",data);



var i=0;
let j=100;
function greet(arr){
    let i=22;
    i=25;
    let j=200;
    console.log(arr);
    arr.forEach(function(item){
        console.log(item);
    });
    console.log(i);
    console.log(j);
}


names=["meghana","suvendru","prasanna","anaya","shreya"]

greet(names)