from django import forms
from .models import *

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['regnom', 'regestreg']
        widgets = {
            'regnom': forms.TextInput(attrs={'class': 'form-control'}),
            'regestreg': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegionForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['regestreg'].widget = forms.HiddenInput()
            self.fields['regestreg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['regestreg'].widget.attrs['readonly'] = True

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['munnom', 'munpreanu', 'munnumviv', 'regcod', 'munestreg']
        widgets = {
            'munnom': forms.TextInput(attrs={'class': 'form-control'}),
            'munpreanu': forms.NumberInput(attrs={'class': 'form-control'}),
            'munnumviv': forms.NumberInput(attrs={'class': 'form-control'}),
            'regcod': forms.Select(attrs={'class': 'form-control'}),
            'munestreg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(MunicipioForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['munestreg'].widget = forms.HiddenInput()
            self.fields['munestreg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['munestreg'].widget.attrs['readonly'] = True


class ZonaUrbanaForm(forms.ModelForm):
    class Meta:
        model = ZonaUrbana
        fields = ['zonnom', 'muncod', 'zonestreg']
        widgets = {
            'zonnom': forms.TextInput(attrs={'class': 'form-control'}),
            'muncod': forms.Select(attrs={'class': 'form-control'}),
            'zonestreg': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ZonaUrbanaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['zonestreg'].widget = forms.HiddenInput()
            self.fields['zonestreg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['zonestreg'].widget.attrs['readonly'] = True



# class ZonaUrbana(models.Model):
#     zoncod = models.AutoField(db_column='ZonCod', primary_key=True, verbose_name="Código")
#     zonnom = models.CharField(db_column='ZonNom', max_length=20, verbose_name="Nombre")
#     muncod = models.ForeignKey(Municipio, on_delete=models.CASCADE, db_column='MunCod', verbose_name="Código de Municipio")
#     zonestreg = models.CharField(db_column='ZonEstReg', max_length=1, default='A', verbose_name="Estado de Registro")

#     class Meta:
#         verbose_name = "Zona Urbana"
#         verbose_name_plural = "Zonas Urbanas"
#         db_table = 'zona_urbana'

#     def __str__(self):
#         return self.zonnom