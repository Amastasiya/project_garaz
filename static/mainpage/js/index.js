//let time = document.createElement("div");
let date = new Date();
/*time.innerHTML = `${date.toLocaleTimeString()} ${date.toLocaleDateString()}`;
document.getElementById("timer1").appendChild(time);
*/
let dtstr = `${date.toLocaleTimeString()} ${date.toLocaleDateString()}`;
document.getElementById("timer1").innerHTML = dtstr;
console.log(dtstr);

/*window.onload = function(){
  window.setInterval(function(){
  var now = new Date();
  var clock = document.getElementById("clock");
  clock.innerHTML = now.toLocaleTimeString();
  },1000);
};*/