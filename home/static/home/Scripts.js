var open;
function Play(file) {
	var door = new Audio(file);
	door.play();
	console.log(file)
}

function clicked(id) {
	if(open != id) {
		$(".category").hide(500);
		$(id).show(250);
		open=id;
	}
}