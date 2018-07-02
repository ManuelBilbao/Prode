var ganador = document.getElementById("id_ganador");
var label_ganador = document.getElementById("label_ganador");
var goles1 = document.getElementById("id_goles1");
var goles2 = document.getElementById("id_goles2");

ganador.setAttribute("class", "form-control");
goles1.addEventListener('change', comprobar);
goles2.addEventListener('change', comprobar);

function comprobar() {
	if (goles1.value == goles2.value) {
		ganador.removeAttribute("style");
		label_ganador.removeAttribute("style");
	} else {
		ganador.setAttribute("style", "display:none");
		label_ganador.setAttribute("style", "display:none");
	}
}

comprobar();