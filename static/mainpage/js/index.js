function insert_date() {
    //let time = document.createElement("div");
    let date = new Date();
    /*time.innerHTML = `${date.toLocaleTimeString()} ${date.toLocaleDateString()}`;
    document.getElementById("timer1").appendChild(time);
    */
    let dtstr = `${date.toLocaleTimeString()} ${date.toLocaleDateString()}`;
    document.getElementById("timer1").innerHTML = dtstr;
    console.log(dtstr);
    setTimeout(insert_date, 500);
}

insert_date();

function cry() {
    console.log("search")
    fetch()

}
/*window.onload = function(){
  window.setInterval(function(){
  var now = new Date();
  var clock = document.getElementById("clock");
  clock.innerHTML = now.toLocaleTimeString();
  },1000);
};*/