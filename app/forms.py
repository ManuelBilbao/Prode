from django import forms
from .models import Prediccion, Partido, Equipo

class FormCambiarPrediccion(forms.ModelForm):
	class Meta:
		model = Prediccion
		fields = ('goles1', 'goles2')