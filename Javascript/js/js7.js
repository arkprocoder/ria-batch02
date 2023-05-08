// or//
// true || true=true
// true || false=true
// false || true=true
// false || false=false
// And 
// true && true=true
// true && false=false
// false && true=false
// false && false=false
/*
console.log("if else loop");
// console.log(22=='22');
const age = 23;

if (age == 2) {
    console.log("age is 22");
} 

else if (age === 22 && age<25) {
    console.log("age is not 22");
} 
else if (age === 23 | age>20 | age<20 && age==25) {
    console.log("age is not 23");
} 
else if (age === 24) {
    console.log("age is not 24");
} 
else {
    console.log("age is not 22")
}


let age1 = "5"; {
    if (age1 == 5) {
        console.log("true");
    } else {
        console.log("false");

    }
}

// can use booleans value also
const doesDrive = false;
if (doesDrive) {
    console.log("can drive")
} else {
    console.log("cannot drive")
}

let bro = false;
let bro1 = false; {
    if (bro || bro1) {
        console.log("true bro")
    } else {
        console.log("false bro")
    }
}
*/

// ternary operator
// let myage=24;
// console.log(myage>20?'yes i am 24':'no i am not 24');
// console.log(myage>20?true:false);
// console.log(true?true:false);
// console.log(false?true:false);



// switch case statements
let myage=29;
switch(myage){

    case 22:
        console.log("22");
        break
    
    case 23:
        console.log("23");
        break

    case 24:
        console.log("24");
        break

    case 25:
        console.log("25");
        break

    default:
        console.log("iam default");
        break
}