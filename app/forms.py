from django import forms
from .models import Prediccion

class FormCambiarPrediccion(forms.ModelForm):
	class Meta:
		model = Prediccion
		fields = ('goles1', 'goles2', 'ganador')