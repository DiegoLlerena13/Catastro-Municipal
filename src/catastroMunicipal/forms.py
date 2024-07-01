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

class TipoPersonaForm(forms.ModelForm):
    class Meta:
        model = TipoPersona
        fields = ['tipperdes', 'tipvivestreg']
        widgets = {
            'tipperdes': forms.TextInput(attrs={'class': 'form-control'}),
            'tipvivestreg': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TipoPersonaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['tipvivestreg'].widget = forms.HiddenInput()
            self.fields['tipvivestreg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['tipvivestreg'].widget.attrs['readonly'] = True

class TipoViviendaForm(forms.ModelForm):
    class Meta:
        model = TipoVivienda
        fields = ['tipvivdes', 'tipvivestreg']
        widgets = {
            'tipvivdes': forms.TextInput(attrs={'class': 'form-control'}),
            'tipvivestreg': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TipoViviendaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['tipvivestreg'].widget = forms.HiddenInput()
            self.fields['tipvivestreg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['tipvivestreg'].widget.attrs['readonly'] = True
            
class ViviendaForm(forms.ModelForm):
    class Meta:
        model = Vivienda
        fields = ['vivcal', 'vivnum', 'vivcodpos', 'vivocu', 'zoncod', 'tipvivcod', 'vivestreg']
        widgets = {
            'vivcal': forms.TextInput(attrs={'class': 'form-control'}),
            'vivnum': forms.NumberInput(attrs={'class': 'form-control'}),
            'vivcodpos': forms.NumberInput(attrs={'class': 'form-control'}),
            'vivocu': forms.Select(attrs={'class': 'form-control'}),
            'zoncod': forms.Select(attrs={'class': 'form-control'}),
            'tipvivcod': forms.Select(attrs={'class': 'form-control'}),
            'vivestreg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(ViviendaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['vivestreg'].widget = forms.HiddenInput()
            self.fields['vivestreg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['vivestreg'].widget.attrs['readonly'] = True    

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['pernom', 'perapepat', 'perapemat', 'famcod', 'tippercod', 'perestreg']

        widgets = {
            'pernom': forms.TextInput(attrs={'class': 'form-control'}),
            'perapepat': forms.TextInput(attrs={'class': 'form-control'}),
            'perapemat': forms.TextInput(attrs={'class': 'form-control'}),
            'famcod': forms.Select(attrs={'class': 'form-control'}),
            'tippercod': forms.Select(attrs={'class': 'form-control'}),
            'perestreg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['perestreg'].widget = forms.HiddenInput()
            self.fields['perestreg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['perestreg'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        famcod = cleaned_data.get('famcod')

        # Verificar la cantidad de integrantes de la familia
        if famcod:
            integrantes_actuales = Persona.objects.filter(famcod=famcod).count()
            num_integrantes_familia = famcod.famnumint  # Obtener el número máximo de integrantes de la familia

            if integrantes_actuales >= num_integrantes_familia:
                raise forms.ValidationError(f"La familia ya tiene registrados {num_integrantes_familia} integrantes. No se pueden agregar más.")

        return cleaned_data
from django import forms
from .models import Casa

class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ['vivcod', 'casesc', 'cascodblo', 'caspla', 'casnumpue', 'casmet', 'famcod', 'casestreg', 'casocu']
        widgets = {
            'vivcod': forms.Select(attrs={'class': 'form-control'}),
            'casesc': forms.NumberInput(attrs={'class': 'form-control'}),
            'cascodblo': forms.TextInput(attrs={'class': 'form-control'}),
            'caspla': forms.NumberInput(attrs={'class': 'form-control'}),
            'casnumpue': forms.NumberInput(attrs={'class': 'form-control'}),
            'casmet': forms.NumberInput(attrs={'class': 'form-control'}),
            'famcod': forms.Select(attrs={'class': 'form-control'}),
            'casestreg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'casocu': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CasaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['casestreg'].widget = forms.HiddenInput()
            self.fields['casestreg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['casestreg'].widget.attrs['readonly'] = True

class PagoTributarioForm(forms.ModelForm):
    class Meta:
        model = PagoTributario
        fields = ['pagtrifec', 'cascod', 'pagtriestreg']
        widgets = {
            'pagtrifec': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cascod': forms.Select(attrs={'class': 'form-control'}),
            'pagtriestreg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(PagoTributarioForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['pagtriestreg'].widget = forms.HiddenInput()
            self.fields['pagtriestreg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['pagtriestreg'].widget.attrs['readonly'] = True