function toggleNav() {
	nav = document.getElementById("sidebar"); 
	main = document.getElementById("main"); 

	if (nav.className == "closed" || nav.className == "") {
		nav.className = "open";
		main.className = "open";
	} else {
		nav.className = "closed";
		main.className = "closed";
	}
}

/*
function toggleLight() {
	let body = document.getElementsByTagName("body")[0];	

	if (light == True) {
		body.style.color = #bbb;
		body.style.background-color = #111;
		light = False;
	} else {
		body.style.color = #000;
		body.style.background-color = #fff;
		light = True;
	}
}*/
