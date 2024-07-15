from django import forms
from .models import Region, Municipio, ZonaUrbana, TipoVivienda, Vivienda, Familia, TipoPersona, Persona, Casa, PagoTributario, Propietario

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['RegNom', 'RegEstReg']
        widgets = {
            'RegNom': forms.TextInput(attrs={'class': 'form-control'}),
            'RegEstReg': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(RegionForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['RegEstReg'].widget = forms.HiddenInput()
            self.fields['RegEstReg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['RegEstReg'].widget.attrs['readonly'] = True    

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['MunNom', 'MunPreAnu', 'MunNumViv', 'RegCod', 'MunEstReg']
        widgets = {
            'MunNom': forms.TextInput(attrs={'class': 'form-control'}),
            'MunPreAnu': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'MunNumViv': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'RegCod': forms.Select(attrs={'class': 'form-control select2'}),
            'MunEstReg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(MunicipioForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['MunEstReg'].widget = forms.HiddenInput()
            self.fields['MunEstReg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['MunEstReg'].widget.attrs['readonly'] = True
            
class ZonaUrbanaForm(forms.ModelForm):
    class Meta:
        model = ZonaUrbana
        fields = ['ZonNom', 'MunCod', 'ZonEstReg']
        widgets = {
            'ZonNom': forms.TextInput(attrs={'class': 'form-control'}),
            'MunCod': forms.Select(attrs={'class': 'form-control select2'}),
            'ZonEstReg': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(ZonaUrbanaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['ZonEstReg'].widget = forms.HiddenInput()
            self.fields['ZonEstReg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['ZonEstReg'].widget.attrs['readonly'] = True
            
class TipoViviendaForm(forms.ModelForm):
    class Meta:
        model = TipoVivienda
        fields = ['TipVivDes', 'TipVivEstReg']
        widgets = {
            'TipVivDes': forms.TextInput(attrs={'class': 'form-control'}),
            'TipVivEstReg': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TipoViviendaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['TipVivEstReg'].widget = forms.HiddenInput()
            self.fields['TipVivEstReg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['TipVivEstReg'].widget.attrs['readonly'] = True
            
class ViviendaForm(forms.ModelForm):
    class Meta:
        model = Vivienda
        fields = ['VivCal', 'VivNum', 'VivCodPos', 'ZonCod', 'TipVivCod', 'VivEstReg']
        widgets = {
            'VivCal': forms.TextInput(attrs={'class': 'form-control'}),
            'VivNum': forms.TextInput(attrs={'class': 'form-control'}),
            'VivCodPos': forms.TextInput(attrs={'class': 'form-control'}),
            'ZonCod': forms.Select(attrs={'class': 'form-control select2'}),
            'TipVivCod': forms.Select(attrs={'class': 'form-control select2'}),
            'VivEstReg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(ViviendaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['VivEstReg'].widget = forms.HiddenInput()
            self.fields['VivEstReg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['VivEstReg'].widget.attrs['readonly'] = True 
            
class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ['FamNom', 'FamNumInt', 'FamEstReg']
        widgets = {
            'FamNom': forms.TextInput(attrs={'class': 'form-control'}),
            'FamNumInt': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'FamEstReg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(FamiliaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['FamEstReg'].widget = forms.HiddenInput()
            self.fields['FamNumInt'].initial = '1'
            self.fields['FamEstReg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['FamEstReg'].widget.attrs['readonly'] = True
            
class TipoPersonaForm(forms.ModelForm):
    class Meta:
        model = TipoPersona
        fields = ['TipPerDes', 'TipPerEstReg']
        widgets = {
            'TipPerDes': forms.TextInput(attrs={'class': 'form-control'}),
            'TipPerEstReg': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(TipoPersonaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['TipPerEstReg'].widget = forms.HiddenInput()
            self.fields['TipPerEstReg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['TipPerEstReg'].widget.attrs['readonly'] = True

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['PerNom', 'FamCod', 'TipPerCod', 'PerEstReg']
        widgets = {
            'PerNom': forms.TextInput(attrs={'class': 'form-control'}),
            'FamCod': forms.Select(attrs={'class': 'form-control select2'}),
            'TipPerCod': forms.Select(attrs={'class': 'form-control select2'}),
            'PerEstReg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['PerEstReg'].widget = forms.HiddenInput()
            self.fields['PerEstReg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['PerEstReg'].widget.attrs['readonly'] = True

    def clean_PerNom(self):
        per_nom = self.cleaned_data['PerNom']
        if not per_nom:
            raise forms.ValidationError("El nombre de la persona no puede ser nulo.")
        return per_nom

    def clean(self):
        cleaned_data = super().clean()
        tip_propietario = cleaned_data.get('TipPerCod')
        fam_cod = cleaned_data.get('FamCod')

        if tip_propietario and tip_propietario.TipPerDes == 'Propietario':
            existing_propietario = Persona.objects.filter(FamCod=fam_cod, TipPerCod=tip_propietario)
            if self.instance.pk:
                existing_propietario = existing_propietario.exclude(pk=self.instance.pk)
            if existing_propietario.exists():
                raise forms.ValidationError("Esta familia ya tiene un propietario asignado.")

class PersonaForm2(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['PerNom', 'FamCod', 'TipPerCod', 'PerEstReg']
        widgets = {
            'PerNom': forms.TextInput(attrs={'class': 'form-control'}),
            'FamCod': forms.Select(attrs={'class': 'form-control','readonly': 'readonly'}),
            'TipPerCod': forms.Select(attrs={'class': 'form-control','readonly': 'readonly'}),
            'PerEstReg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(PersonaForm2, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['PerEstReg'].widget = forms.HiddenInput()
            self.fields['PerEstReg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['PerEstReg'].widget.attrs['readonly'] = True

    def clean_PerNom(self):
        per_nom = self.cleaned_data['PerNom']
        if not per_nom:
            raise forms.ValidationError("El nombre de la persona no puede ser nulo.")
        return per_nom

            
class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ['CasEsc', 'CasCodBlo', 'CasPla', 'CasNumPue', 'CasMet', 'VivCod', 'FamCod', 'CasEstReg', 'CasOcu']
        widgets = {
            'VivCod': forms.Select(attrs={'class': 'form-control select2'}),
            'CasEsc': forms.TextInput(attrs={'class': 'form-control'}),
            'CasCodBlo': forms.TextInput(attrs={'class': 'form-control'}),
            'CasPla': forms.TextInput(attrs={'class': 'form-control'}),
            'CasNumPue': forms.TextInput(attrs={'class': 'form-control'}),
            'CasMet': forms.NumberInput(attrs={'class': 'form-control'}),
            'FamCod': forms.Select(attrs={'class': 'form-control select2'}),
            'CasEstReg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'CasOcu': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CasaForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['CasEstReg'].widget = forms.HiddenInput()
            self.fields['CasEstReg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['CasEstReg'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        viv_cod = cleaned_data.get('VivCod')
        tip_viv_des = viv_cod.TipVivCod.TipVivDes if viv_cod and viv_cod.TipVivCod else None

        # Validaciones específicas según el tipo de vivienda
        if tip_viv_des == "Particular":
            existing_casa = Casa.objects.filter(VivCod=viv_cod)
            if self.instance.pk:
                existing_casa = existing_casa.exclude(pk=self.instance.pk)
            if existing_casa.exists():
                raise forms.ValidationError("Ya existe una casa asignada a esta vivienda particular.")
            if cleaned_data.get('CasEsc') or cleaned_data.get('CasCodBlo') or cleaned_data.get('CasPla') or cleaned_data.get('CasNumPue'):
                raise forms.ValidationError("Los campos CasEsc, CasCodBlo, CasPla y CasNumPue deben estar vacíos si la vivienda no es de tipo BloqueCasa.")

        elif tip_viv_des == "BloqueCasa":
            if not cleaned_data.get('CasEsc') or not cleaned_data.get('CasCodBlo') or not cleaned_data.get('CasPla') or not cleaned_data.get('CasNumPue'):
                raise forms.ValidationError("Los campos CasEsc, CasCodBlo, CasPla y CasNumPue son obligatorios si la vivienda es de tipo 'BloqueCasa'.")

class PagoTributarioForm(forms.ModelForm):
    class Meta:
        model = PagoTributario
        fields = ['PagTriFec', 'CasCod', 'PagTriIngFam', 'PagTriCat', 'PagTriPag', 'PagTriEstReg']
        widgets = {
            'PagTriFec': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'dd/mm/aaaa'}),
            'CasCod': forms.Select(attrs={'class': 'form-control select2'}),
            'PagTriIngFam': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'PagTriCat': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'PagTriPag': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'PagTriEstReg': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PagoTributarioForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['PagTriEstReg'].widget = forms.HiddenInput()
            self.fields['PagTriEstReg'].initial = 'debe'
            self.fields['PagTriCat'].widget.attrs['readonly'] = True
            self.fields['PagTriPag'].widget.attrs['readonly'] = True
        else:  # Si se está editando una instancia existente
            self.fields['PagTriEstReg'].widget.attrs['readonly'] = True    

    def clean(self):
        cleaned_data = super().clean()
        cas_cod = cleaned_data.get('CasCod')

        # Validar que no haya duplicados de casa para pagos tributarios
        if PagoTributario.objects.filter(CasCod=cas_cod).exists() and not self.instance.pk:
            raise forms.ValidationError("Esta casa ya tiene un pago tributario asignado.")

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['ProMonIngFam', 'PerCod', 'ProEstReg']
        widgets = {
            'ProMonIngFam': forms.NumberInput(attrs={'class': 'form-control'}),
            'PerCod': forms.Select(attrs={'class': 'form-control select2'}),
            'ProEstReg': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(PropietarioForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # Si se está creando una nueva instancia
            self.fields['ProEstReg'].widget = forms.HiddenInput()
            self.fields['ProEstReg'].initial = 'A'
        else:  # Si se está editando una instancia existente
            self.fields['ProEstReg'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        per_cod = cleaned_data.get('PerCod')

        # Validar que ProMonIngFam no sea nulo
        if not cleaned_data.get('ProMonIngFam'):
            raise forms.ValidationError("El campo ProMonIngFam no puede ser nulo.")

        # Validar que la persona tiene el tipo "Propietario"
        if per_cod.TipPerCod.TipPerDes != "Propietario":
            raise forms.ValidationError("La persona seleccionada no tiene el tipo de persona 'Propietario'.")

        # Validar que la persona no sea propietario de más de una familia
        if Propietario.objects.filter(PerCod=per_cod).exists() and not self.instance.pk:
            raise forms.ValidationError("La persona seleccionada ya es propietario de una familia.")
        
class ConsultaViviendaForm(forms.ModelForm):
    vivienda = forms.ModelChoiceField(queryset=Vivienda.objects.all(), widget=forms.Select(attrs={'class': 'form-control select2'}))

    class Meta:
        model = Vivienda
        fields = ['vivienda']

class ConsultaZonaForm(forms.ModelForm):
    zona = forms.ModelChoiceField(queryset=ZonaUrbana.objects.all(), widget=forms.Select(attrs={'class': 'form-control select2'}))

    class Meta:
        model = ZonaUrbana
        fields = ['zona']

class ConsultaMunicipioForm(forms.ModelForm):
    municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), widget=forms.Select(attrs={'class': 'form-control select2'}))

    class Meta:
        model = Municipio
        fields = ['municipio']

class ConsultaRegionForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), widget=forms.Select(attrs={'class': 'form-control select2'}))

    class Meta:
        model = Region
        fields = ['region']


    