from django.contrib import admin
from .models import Torneo, Equipo, Partido, Prediccion, Puntaje

# Register your models here.
admin.site.register(Torneo)
admin.site.register(Equipo)
admin.site.register(Partido)
admin.site.register(Prediccion)
admin.site.register(Puntaje)