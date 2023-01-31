function insert_date() {
    //let time = document.createElement("div");
    let date = new Date();
    /*time.innerHTML = `${date.toLocaleTimeString()} ${date.toLocaleDateString()}`;
    document.getElementById("timer1").appendChild(time);
    */
    let dtstr = `${date.toLocaleTimeString()} ${date.toLocaleDateString()}`;
    document.getElementById("timer1").innerHTML = dtstr;
    //console.log(dtstr);
    setTimeout(insert_date, 500);
}

insert_date();

function cry() {
    console.log("search");
    let user = {
        name: 'Igor',// достать данные из базы!!!
        phone: '444'
    };
    let tokens = document.getElementsByName('csrfmiddlewaretoken');
    console.log(tokens[0].value);
    fetch('/mainpage/', {
        method: 'POST',
		headers: {
	        'Content-Type': 'application/json',
			'X-CSRFToken': tokens[0].value,
            'Accept': 'application/json',
        },
        body: JSON.stringify({
            name: 'Igor',// достать данные из базы!!!
            phone: '444'
        })
    }).then(response => {
			console.log(response);
			return response.json();
	}).then(result => {
		console.log(result)
	});
}
/*window.onload = function(){
  window.setInterval(function(){
  var now = new Date();
  var clock = document.getElementById("clock");
  clock.innerHTML = now.toLocaleTimeString();
  },1000);
};*/