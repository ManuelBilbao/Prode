var clasifica = document.getElementById("id_clasifica");
var label_clasifica = document.getElementById("label-clasifica");
var goles1 = document.getElementById("id_goles1");
var goles2 = document.getElementById("id_goles2");

clasifica.setAttribute("class", "form-control");
goles1.addEventListener('change', comprobar);
goles2.addEventListener('change', comprobar);

function comprobar() {
	if (goles1.value == goles2.value) {
		clasifica.removeAttribute("style");
		label_clasifica.removeAttribute("style");
	} else {
		clasifica.setAttribute("style", "display:none");
		label_clasifica.setAttribute("style", "display:none");
	}
}

comprobar();