let time = document.createElement("div");
let date = new Date();
time.innerHTML = `${date.toLocaleTimeString()} ${date.toLocaleDateString()}`;
document.getElementBuId("timer1").appendChild(time)
