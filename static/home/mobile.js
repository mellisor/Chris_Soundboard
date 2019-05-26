var open;

$(document).ready(function(){
	var x = document.getElementsByClassName("catButton");
	var i;
	for(i = 0; i < x.length; i++)
	{
		setTimeout(function(elem){
			$("#" + elem).fadeIn(200);
		},i*200,x[i].id);
	}
});

function catClick(cat) {
	open = cat.id + "Div";
	var x = document.getElementsByClassName("catButton");
	var i;
	for(i = 0; i < x.length; i++)
	{	
		setTimeout(function(elem){
			$("#" + elem).fadeOut(100);
		},i*50,x[x.length-1-i].id);
	}
	var s = document.getElementById(cat.id + "Div").childNodes;
	setTimeout(function(i,s){
		for(i = 0; i < s.length; i++)
		{
			setTimeout(function(elem){
				if(elem.id != "")
					$("#" + elem.id).fadeIn(200,checkOpen(elem));
			},i*20,s[i]);
		}
	},x.length*50 + 100,i,s);
};

function goback(id) {
	open = "";
	var all = document.getElementById(id).childNodes;
	var i;
	for(i = 0; i < all.length; i++)
	{
		if(all[i].id == "")
		{
			continue;
		}
		$("#" + all[i].id).fadeOut(200);
	}
	setTimeout(function(){
		var cats = document.getElementsByClassName('catButton');
		var i;
		for(i = 0; i < cats.length; i++)
		{
			$("#" + cats[i].id).fadeIn(200);
		}
	},200);
};

function checkOpen(node) {
	if(node.parentNode.id != open){
		setTimeout(function(elem){
			console.log("#" + elem.id);
			$("#" + elem.id).fadeOut();
		},400,elem);	
	}
}

function Play(sound) {
	var f = new Audio(sound);
	f.play();
};
