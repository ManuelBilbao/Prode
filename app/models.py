from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Torneo(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Equipo(models.Model):
	nombre = models.CharField(max_length=100)
	torneos = models.ManyToManyField(Torneo)

	def __str__(self):
		return self.nombre

class Partido(models.Model):
	equipo1 = models.ForeignKey(Equipo, related_name='equipo1', on_delete=models.CASCADE)
	equipo2 = models.ForeignKey(Equipo, related_name='equipo2', on_delete=models.CASCADE)
	torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
	grupo = models.CharField(max_length=10)
	fecha = models.SmallIntegerField();
	horario = models.DateTimeField();
	goles1 = models.SmallIntegerField(null=True, blank=True)
	goles2 = models.SmallIntegerField(null=True, blank=True)
	eliminatoria = models.BooleanField(default = False)
	penales1 = models.SmallIntegerField(null = True, blank = True)
	penales2 = models.SmallIntegerField(null = True, blank = True)
	fase_eliminatoria = models.SmallIntegerField(null = True, blank = True)

	def se_jugo(self):
		return self.horario <= timezone.now()

	def __str__(self):
		return self.equipo1.nombre + " - " + self.equipo2.nombre


class Prediccion(models.Model):
	usuario = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE)
	torneo = models.ForeignKey(Torneo, related_name='torneo', on_delete=models.CASCADE)
	partido = models.ForeignKey(Partido, related_name='partido', on_delete=models.CASCADE)
	goles1 = models.SmallIntegerField()
	goles2 = models.SmallIntegerField()
	ganador = models.ForeignKey(Equipo, related_name='equipo_ganador', on_delete=models.CASCADE, null=True, blank = True, default=None)

	def __str__(self):
		return self.usuario.username + " -> " + self.partido.equipo1.nombre + " - " + self.partido.equipo2.nombre

class Puntaje(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	plenos = models.SmallIntegerField(default = 0)
	resultados = models.SmallIntegerField(default = 0)
	penales = models.SmallIntegerField(default = 0)
	error_clasificado = models.SmallIntegerField(default = 0)

	def __str__(self):
		return self.usuario.username