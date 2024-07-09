from django import forms
from django.core.exceptions import ValidationError
from .models import *
from decimal import Decimal
from django.utils.html import format_html

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
            'regcod': forms.Select(attrs={'class': 'form-control select2'}),
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
            'muncod': forms.Select(attrs={'class': 'form-control select2'}),
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
            'zoncod': forms.Select(attrs={'class': 'form-control select2'}),
            'tipvivcod': forms.Select(attrs={'class': 'form-control select2'}),
            'vivestreg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(ViviendaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['vivestreg'].widget = forms.HiddenInput()
            self.fields['vivestreg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['vivestreg'].widget.attrs['readonly'] = True 

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ['famnom', 'famnumint', 'famestreg']

        widgets = {
            'famnom': forms.TextInput(attrs={'class': 'form-control'}),
            'famnumint': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'famestreg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(FamiliaForm, self).__init__(*args, **kwargs)
        self.fields['famnumint'].widget.attrs['readonly'] = True  # Make famnumint read-only
        if not self.instance.pk:  # If creating a new instance
            self.fields['famestreg'].widget = forms.HiddenInput()
            self.fields['famestreg'].initial = 'A'
        else:  # If editing an existing instance
            self.fields['famestreg'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        if self.instance.pk:  # If editing an existing instance
            # Automatically update the number of integrantes
            cleaned_data['famnumint'] = self.instance.persona_set.count()

        return cleaned_data
    
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['pernom', 'perapepat', 'perapemat', 'famcod', 'tippercod', 'perestreg']

        widgets = {
            'pernom': forms.TextInput(attrs={'class': 'form-control'}),
            'perapepat': forms.TextInput(attrs={'class': 'form-control'}),
            'perapemat': forms.TextInput(attrs={'class': 'form-control'}),
            'famcod': forms.Select(attrs={'class': 'form-control select2'}),
            'tippercod': forms.Select(attrs={'class': 'form-control select2'}),
            'perestreg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # If creating a new instance
            self.fields['perestreg'].widget = forms.HiddenInput()
            self.fields['perestreg'].initial = 'A'
        else:  # If editing an existing instance
            self.fields['perestreg'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        # No need to verify the maximum number of family members anymore
        return cleaned_data

class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ['vivcod', 'casesc', 'cascodblo', 'caspla', 'casnumpue', 'casmet', 'famcod', 'casestreg', 'casocu']
        widgets = {
            'vivcod': forms.Select(attrs={'class': 'form-control select2'}),
            'casesc': forms.NumberInput(attrs={'class': 'form-control'}),
            'cascodblo': forms.TextInput(attrs={'class': 'form-control'}),
            'caspla': forms.NumberInput(attrs={'class': 'form-control'}),
            'casnumpue': forms.NumberInput(attrs={'class': 'form-control'}),
            'casmet': forms.NumberInput(attrs={'class': 'form-control'}),
            'famcod': forms.Select(attrs={'class': 'form-control select2'}),
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

    def clean(self):
        cleaned_data = super().clean()
        famcod = cleaned_data.get('famcod')

        # Validar que solo una familia puede tener una casa
        existing_casa = Casa.objects.filter(famcod=famcod)
        if self.instance.pk:
            existing_casa = existing_casa.exclude(pk=self.instance.pk)  # Excluir la instancia actual al editar
        if existing_casa.exists():
            raise ValidationError("Esta familia ya tiene asignada una casa.")

        return cleaned_data

    def save(self, *args, **kwargs):
        try:
            self.full_clean()  # Llama a clean() antes de guardar para validar
            super().save(*args, **kwargs)
        except ValidationError as e:
            # Imprimir el error pero no redirigir a la página de error
            print(f"Error al guardar la casa: {e}")
            raise  # Re-lanza la excepción para que la vista pueda manejarla

class PagoTributarioForm(forms.ModelForm):
    class Meta:
        model = PagoTributario
        fields = ['pagtrifec', 'cascod', 'pagtriestreg']
        widgets = {
            'pagtrifec': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'dd/mm/aaaa'}),
            'cascod': forms.Select(attrs={'class': 'form-control select2'}),
            'pagtriestreg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(PagoTributarioForm, self).__init__(*args, **kwargs)
        if self.instance.pk:  # Si se está editando una instancia existente
            self.fields['pagtrifec'].widget.attrs['value'] = self.instance.pagtrifec.strftime('%Y-%m-%d')
            self.fields['pagtriestreg'].widget.attrs['readonly'] = True
        else:  # Si se está creando una nueva instancia
            self.fields['pagtriestreg'].widget = forms.HiddenInput()
            self.fields['pagtriestreg'].initial = 'A'

    
class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['promoningfam', 'percod', 'famcod', 'proestreg']
        widgets = {
            'promoningfam': forms.NumberInput(attrs={'class': 'form-control'}),
            'percod': forms.Select(attrs={'class': 'form-control select2'}),
            'famcod': forms.Select(attrs={'class': 'form-control select2'}),
            'proestreg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(PropietarioForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['proestreg'].widget = forms.HiddenInput()
            self.fields['proestreg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['proestreg'].widget.attrs['readonly'] = True
            
    def clean_promoningfam(self):
        promoningfam = self.cleaned_data['promoningfam']
        if promoningfam <= Decimal('0'):
            raise forms.ValidationError("El monto de ingreso familiar debe ser mayor que cero.")
        return promoningfam

    def clean(self):
        cleaned_data = super().clean()
        famcod = cleaned_data.get('famcod')
        percod = cleaned_data.get('percod')

        # Validar que la persona tiene el tipo "Propietario"
        if percod and percod.tippercod.tipperdes != "Propietario":
            raise forms.ValidationError("La persona seleccionada no tiene el tipo de persona 'Propietario'.")

        # Validar que solo puede haber un propietario por familia
        if famcod and Propietario.objects.filter(famcod=famcod).exists() and not self.instance.pk:
            raise forms.ValidationError("Ya existe un propietario para esta familia.")

        # Validar que la persona no sea propietario de más de una familia
        if percod and Propietario.objects.filter(percod=percod).exists() and not self.instance.pk:
            raise forms.ValidationError("La persona seleccionada ya es propietario de otra familia.")
        return cleaned_data
    