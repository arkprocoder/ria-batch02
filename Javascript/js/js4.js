console.log("js-typeconversion");
let num='123'
console.log(typeof num);
num=Number(num);
console.log(typeof num);
var n=50;
console.log(n,typeof n);
n=String(n);
console.log(n,typeof n);
let name="anes";
console.log(Number(name));

let array=[1,2,3,4,5];
array=String(array);
console.log(array);
console.log(array.length);

let i=10;
i=i.toString();
console.log(i,typeof(i));

let isAdmin=false;
console.log(isAdmin,typeof isAdmin);
// isAdmin=isAdmin.toString();
isAdmin=Number(isAdmin);
console.log(isAdmin,typeof isAdmin);


let d='234.567890';
d=Number(234.566890);
console.log(d);
console.log(d.toFixed(2));

let nm=parseFloat('234');
console.log(nm,typeof nm);

// type coercion

let a ='aa'
let b=22;
console.log(a+b);