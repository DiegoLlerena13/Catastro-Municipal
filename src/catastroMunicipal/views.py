from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def base(request):
    return render(request, 'cm/base.html')

def main(request):
    return render(request, 'main.html')

def region_list(request):
    regiones = Region.objects.all()
    return render(request, 'region_list.html', {'regiones': regiones})

def municipio_list(request):
    municipios = Municipio.objects.all()
    return render(request, 'municipio_list.html', {'municipios': municipios})

def zona_urbana_list(request):
    zonas_urbanas = ZonaUrbana.objects.all()
    return render(request, 'zona_urbana_list.html', {'zonas_urbanas': zonas_urbanas})

def tipo_vivienda_list(request):
    tipos_vivienda = TipoVivienda.objects.all()
    return render(request, 'tipo_vivienda_list.html', {'tipos_vivienda': tipos_vivienda})

def vivienda_list(request):
    viviendas = Vivienda.objects.all()
    return render(request, 'vivienda_list.html', {'viviendas': viviendas})

def casa_list(request):
    casas = Casa.objects.all()
    return render(request, 'casa_list.html', {'casas': casas})

def familia_list(request):
    familias = Familia.objects.all()
    return render(request, 'familia_list.html', {'familias': familias})

def persona_list(request):
    personas = Persona.objects.all()
    return render(request, 'persona_list.html', {'personas': personas})

def tipo_persona_list(request):
    tipos_persona = TipoPersona.objects.all()
    return render(request, 'tipo_persona_list.html', {'tipos_persona': tipos_persona})

def propietario_list(request):
    propietarios = Propietario.objects.all()
    return render(request, 'propietario_list.html', {'propietarios': propietarios})

def pago_tributario_list(request):
    pagos_tributarios = PagoTributario.objects.all()
    return render(request, 'pago_tributario_list.html', {'pagos_tributarios': pagos_tributarios})

