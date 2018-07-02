from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Equipo, Partido, Prediccion, Puntaje
from django.db.models import F

EMPATE = 0

def calcular_ganador(goles1, goles2):
	if goles1 > goles2:
		ganador = 1
	elif goles2 > goles1:
		ganador = 2
	else:
		ganador = EMPATE

	return ganador

@receiver(post_save, sender = User)
def nuevo_usuario(sender, instance, **kwargs):
	if kwargs['created']:
		Puntaje.objects.create(usuario = instance)

@receiver(post_save, sender = Partido)
def actualizar_puntajes(sender, instance, **kwargs):
	if instance.goles1 == None or instance.goles2 == None:
		return

	partido = instance
	predicciones = Prediccion.objects.filter(partido = partido)
	puntajes = Puntaje.objects.all()

	ganador_real = calcular_ganador(partido.goles1, partido.goles2)

	for prediccion in predicciones:
		ganador_prediccion = calcular_ganador(prediccion.goles1, prediccion.goles2)

		if prediccion.goles1 == partido.goles1 and prediccion.goles2 == partido.goles2:
			puntajes.filter(usuario = prediccion.usuario).update(plenos = F('plenos') + 1)
		elif ganador_prediccion == ganador_real:
			puntajes.filter(usuario = prediccion.usuario).update(resultados = F('resultados') + 1)

		if partido.eliminatoria:

			if ganador_real == 1:
				ganador = partido.equipo1
			elif ganador_real == 2:
				ganador = partido.equipo2
			else: #Si es empate miro los penales
				if partido.penales1 > partido.penales2:
					ganador = partido.equipo1
				else:
					ganador = partido.equipo2

			if ganador_real == EMPATE and ganador == prediccion.ganador:
				puntajes.filter(usuario = prediccion.usuario).update(penales = F('penales') + 1)

			if ganador != prediccion.ganador:
				puntajes.filter(usuario = prediccion.usuario).update(error_clasificado = F('error_clasificado') + 1)