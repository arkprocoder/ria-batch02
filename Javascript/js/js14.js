console.log("events");
document.getElementById("ark").addEventListener("click", function(e) {
    console.log("you have clicked arkprocoder");
    let v=document.getElementById("ark")
    v.setAttribute('style','color:red;') 
    v1 = e.target;
    console.log(v1);
    v1 = e.target.className;
    console.log(v1);
    v1 = e.target.id;
    console.log(v1);
    v1 = e.offsetX;
    console.log(v1);
    v1 = e.offsetY;
    console.log(v1);
    v1 = e.clientX;
    console.log(v1);
    v1 = e.clientY;
    console.log(v1);
    v1 = e.target.className;
    console.log(v1);
    v1 = Array.from(e.target.classList);
    console.log(v1);

})

document.getElementById("dj").addEventListener("click", function() {
    alert("Event Occured")
    document.getElementById("dj").innerHTML = "<b> Expert in Django</b>";
    document.getElementById("dj").setAttribute('style','color:red;') 

    
})

function bigImg(x) {
    x.setAttribute('style','color:red;') 
  }
  
function normalImg(x) {
    x.setAttribute('style','color:yellow;') 
  }

function insertData(){
    data=document.getElementById("mytext")
    inpdata=document.getElementById("inptxt").value
    data.innerHTML=inpdata
}