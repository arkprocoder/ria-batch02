console.log("js-arrays");
let data= [10,20,70,30,60,50,'apple','banana',true,10,20];
console.log(data,typeof data);
console.log(data[2]);
console.log(data.length);
console.log(Array.isArray([1,23]));
data[12]='ria';
console.log(data);

let value=data.indexOf(170)
console.log(value);
let value1=data.lastIndexOf(10)
console.log(value1);
data.push(150);
console.log(data);
data.pop();
console.log(data);
data.unshift('javascript');
console.log(data);

data.splice(2,4);
console.log(data);

var a1=[1,2,3,4];
var a2=[8,7,6,5];
a1=a1.concat(a2);
console.log(a1);
console.log(a2);
console.log(a1.sort());
console.log(a1.toString());

let myDetails ={
    name:"Ria",
    location:"Bangalore",
    since:1999,
    isActive:true,
    courses:['python','java']
}

console.log(myDetails,typeof myDetails);