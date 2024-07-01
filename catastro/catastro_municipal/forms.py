from django import forms
from .models import ZonaUrbana, OtroModelo

class ZonaUrbanaForm(forms.ModelForm):
    class Meta:
        model = ZonaUrbana
        fields = ['codzona', 'nomzona']

class OtroModeloForm(forms.ModelForm):
    class Meta:
        model = OtroModelo
        fields = ['campo1', 'campo2']
