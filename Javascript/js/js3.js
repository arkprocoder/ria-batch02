console.log('data types in javascript');
// primitive datatype
var name='anees';
console.log(name,typeof(name));
var sal=125478.25874;
console.log(sal,typeof(sal));
var working=true;
console.log(working,typeof(working));
let null1=null
console.log(null1,typeof(null1));
let undef=undefined;
console.log(undef,typeof(undef));

//reference data types
var mydata=[10,202,123];
console.log(mydata, typeof(mydata));

let details={
    name:'aadithyaa',
    age:22
}
console.log(details,typeof(details));

function greet(){
    console.log('good morning');
}
console.log(greet(),typeof(greet));

let date=new Date();
console.log(date);
console.log(typeof(date));