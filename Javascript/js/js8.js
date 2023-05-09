console.log("welcome to loops");
// for

// for(datatype:initilization,expression,increment/decrement){
//     logic
// }
/*
for(let i=0;i<=20;i++){
    console.log(i)
}
for(let i=20;i>0;i--){
    console.log(i)
}
*/

let k=0; //initialization
while(k<10){  //checking expression if true
    console.log(k);  //run the logic
    k=k+1;
}

console.log("do-while loop");
let j=0 //initialization
do{
    console.log("do this first")
    console.log(j);
    j+=1;  //run the logic
}

while(j<11) //check the expression if true repeat initialization


// let myarray=["apple","banana","orange","pineapple"]
// for(let i=0;i<myarray.length;i++){
//     console.log(`Fruits in my array ${i} index ${myarray[i]}`);
// }

// break statements

// let s = 0;
// do {
//     if (s === 5) {
//         break;
//     }
//     console.log(s + 1);
//     s += 1;

// }
//  while (s < 100);
// console.log("done appa");





// continue statements

let r = 0;
do {
    if (r === 5) {
        r=r+1;
        continue
    }
    r=r+1;
    console.log(r);

} while (r < 10);


for(let i=1;i<=20;i++)
{
    if(i==15){
        continue
    }
    if(i==18){
        break
    }
    console.log(i);
}




//for each loop
// let arraylist=[1,2,3,4,5,6,7,8,9,10];
// arraylist.forEach(function(item,index,array){
//     console.log(item,index,array);
// })
/*
let arraylist=[1,2,3,4,5,6,7,8,9,10];
arraylist.forEach(function(item){
    console.log(item);
})



let myDetails ={
    name:"Ria",
    location:"Bangalore",
    since:1999,
    isActive:true,
    courses:['python','java']
}
for(let k in myDetails){
    console.log(`${k} value is ${myDetails[k]}`);
}
*/