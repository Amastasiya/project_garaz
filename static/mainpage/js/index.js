let time = document.createElement("div");
let date = new Date();
time.innerHTML = `${date.toLocaleTimeString()} ${date.toLocaleDateString()}`;
document.getElementBuId("timer1").appendChild(time)


window.onload = function(){
  window.setInterval(function(){
  var now = new Date();
  var clock = document.getElementById("clock");
  clock.innerHTML = now.toLocaleTimeString();
  },1000);
};