from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F, Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormCambiarPrediccion
from .models import Equipo, Partido, Torneo, Prediccion, Puntaje

VALOR_PLENO = 3
VALOR_RESULTADO = 1
VALOR_PENAL = 1
VALOR_ERRAR_CLASIFICADO = -1

@login_required
def actualizar_prediccion(request, partido_pk, prediccion_pk):
	partido = get_object_or_404(Partido, pk = partido_pk)

	if partido.se_jugo():
		return redirect('fixture')

	try:
		prediccion = Prediccion.objects.get(usuario = request.user, pk = prediccion_pk, partido = partido)
	except Prediccion.DoesNotExist:
		return redirect('crear_prediccion', partido_pk)

	if request.method == "POST":
		form = FormCambiarPrediccion(request.POST, instance = prediccion)
		if form.is_valid():
			actualizacion = form.save(commit = False)
			form.save()
			return redirect('fixture')
	else:
		form = FormCambiarPrediccion(instance = prediccion)
		form.fields['ganador'].queryset = Equipo.objects.filter(Q(pk = partido.equipo1.pk) | Q(pk = partido.equipo2.pk))

	return render(request, 'app/cambiar_prediccion.html', {'form': form, 'partido': partido})

@login_required
def crear_prediccion(request, partido_pk):
	mundial = Torneo.objects.get(nombre = 'Mundial')
	partido = get_object_or_404(Partido, pk = partido_pk)
	try: #Si ya existe una prediccion de ese usuario para ese partido
		prediccion = Prediccion.objects.get(usuario = request.user, partido = partido_pk)
		return redirect('actualizar_prediccion', partido_pk, prediccion.pk)
	except Prediccion.DoesNotExist:
		pass

	if request.method == "POST":
		form = FormCambiarPrediccion(request.POST)
		if form.is_valid():
			nuevo = form.save(commit = False)
			nuevo.usuario = request.user
			nuevo.torneo = mundial
			nuevo.partido = partido
			nuevo.save()
			return redirect('fixture')
	else:
		form = FormCambiarPrediccion()
		form.fields['ganador'].queryset = Equipo.objects.filter(Q(pk = partido.equipo1.pk) | Q(pk = partido.equipo2.pk))

	return render(request, 'app/cambiar_prediccion.html', {'form': form, 'partido': partido})

def puntos(request):
	puntajes = Puntaje.objects.all().annotate(puntos = VALOR_PLENO * F('plenos') + VALOR_RESULTADO * F('resultados') + VALOR_PENAL * F('penales') + VALOR_ERRAR_CLASIFICADO * F('error_clasificado')).order_by('-puntos', '-plenos', '-resultados')

	return render(request, 'app/puntos.html', {'puntajes': puntajes})

@login_required
def fixture(request):
	usuario = request.user
	mundial = Torneo.objects.get(nombre = 'Mundial')
	partidos = Partido.objects.filter(torneo = mundial).order_by('eliminatoria', 'fase_eliminatoria', 'grupo', 'fecha', 'horario')
	predicciones = Prediccion.objects.filter(usuario = usuario, torneo = mundial).order_by('partido__eliminatoria', 'partido__fase_eliminatoria', 'partido__grupo', 'partido__fecha', 'partido__horario')

	i = 0
	j = 0
	partidos_con_predicciones = []
	while i < partidos.count() and j < predicciones.count():
		partidos_con_predicciones.append(partidos[i])
		if partidos[i].pk == predicciones[j].partido.pk:
			partidos_con_predicciones[i].prediccion = predicciones[j]
			j += 1

		i += 1

	while i < partidos.count():
		partidos_con_predicciones.append(partidos[i])
		i += 1

	return render(request, 'app/fixture.html', {'partidos': partidos_con_predicciones})

@login_required
def ver_predicciones(request, partido_pk):
	partido = get_object_or_404(Partido, pk = partido_pk)
	predicciones = Prediccion.objects.filter(partido = partido).order_by('usuario__username')

	return render(request, 'app/ver_predicciones.html', {'predicciones': predicciones})