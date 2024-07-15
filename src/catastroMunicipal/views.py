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

def region_create(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            region = form.save(commit=False)
            region.regestreg = 'A'  # Asegurarse de que el estado por defecto sea 'A'
            region.save()
            return redirect('region_list')
    else:
        form = RegionForm()
    return render(request, 'region_form.html', {'form': form})

def region_update(request, pk):
    region = get_object_or_404(Region, pk=pk)
    if request.method == "POST":
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            form.save()
            return redirect('region_list')
    else:
        form = RegionForm(instance=region)
    return render(request, 'region_form.html', {'form': form, 'region': region})

def region_delete(request, pk):
    region = get_object_or_404(Region, pk=pk)
    if request.method == "POST":
        region.delete()
        return redirect('region_list')
    return render(request, 'region_delete.html', {'region': region})

def municipio_create(request):
    if request.method == "POST":
        form = MunicipioForm(request.POST)
        if form.is_valid():
            municipio = form.save(commit=False)
            municipio.munestreg = 'A'  # Asegurarse de que el estado por defecto sea 'A'
            municipio.save()
            return redirect('municipio_list')
    else:
        form = MunicipioForm()
    return render(request, 'municipio_form.html', {'form': form})

def municipio_update(request, pk):
    municipio = get_object_or_404(Municipio, pk=pk)
    if request.method == "POST":
        form = MunicipioForm(request.POST, instance=municipio)
        if form.is_valid():
            form.save()
            return redirect('municipio_list')
    else:
        form = MunicipioForm(instance=municipio)
    return render(request, 'municipio_form.html', {'form': form})

def municipio_delete(request, pk):
    municipio = get_object_or_404(Municipio, pk=pk)
    if request.method == "POST":
        municipio.delete()
        return redirect('municipio_list')
    return render(request, 'municipio_delete.html', {'municipio': municipio})

def zona_urbana_create(request):
    if request.method == "POST":
        form = ZonaUrbanaForm(request.POST)
        if form.is_valid():
            zona_urbana = form.save(commit=False)
            zona_urbana.zonurbestreg = 'A'  # Asegurarse de que el estado por defecto sea 'A'
            zona_urbana.save()
            return redirect('zona_urbana_list')
    else:
        form = ZonaUrbanaForm()
    return render(request, 'zona_urbana_form.html', {'form': form})

def zona_urbana_update(request, pk):
    zona_urbana = get_object_or_404(ZonaUrbana, pk=pk)
    if request.method == "POST":
        form = ZonaUrbanaForm(request.POST, instance=zona_urbana)
        if form.is_valid():
            form.save()
            return redirect('zona_urbana_list')
    else:
        form = ZonaUrbanaForm(instance=zona_urbana)
    return render(request, 'zona_urbana_form.html', {'form': form})

def zona_urbana_delete(request, pk):
    zona_urbana = get_object_or_404(ZonaUrbana, pk=pk)
    if request.method == "POST":
        zona_urbana.delete()
        return redirect('zona_urbana_list')
    return render(request, 'zona_urbana_delete.html', {'zona_urbana': zona_urbana})

def vivienda_create(request):
    if request.method == "POST":
        form = ViviendaForm(request.POST)
        if form.is_valid():
            vivienda = form.save(commit=False)
            vivienda.vivestreg = 'A'  # Asegurarse de que el estado por defecto sea 'A'
            vivienda.save()
            return redirect('vivienda_list')
    else:
        form = ViviendaForm()
    return render(request, 'vivienda_form.html', {'form': form})

def vivienda_update(request, pk):
    vivienda = get_object_or_404(Vivienda, pk=pk)
    if request.method == "POST":
        form = ViviendaForm(request.POST, instance=vivienda)
        if form.is_valid():
            form.save()
            return redirect('vivienda_list')
    else:
        form = ViviendaForm(instance=vivienda)
    return render(request, 'vivienda_form.html', {'form': form})

def vivienda_delete(request, pk):
    vivienda = get_object_or_404(Vivienda, pk=pk)
    if request.method == "POST":
        vivienda.delete()
        return redirect('vivienda_list')
    return render(request, 'vivienda_delete.html', {'vivienda': vivienda})

def tipo_persona_create(request):
    if request.method == "POST":
        form = TipoPersonaForm(request.POST)
        if form.is_valid():
            tipo_persona = form.save(commit=False)
            tipo_persona.tipperestreg = 'A'  # Asegurarse de que el estado por defecto sea 'A'
            tipo_persona.save()
            return redirect('tipo_persona_list')
    else:
        form = TipoPersonaForm()
    return render(request, 'tipo_persona_form.html', {'form': form})

def tipo_persona_update(request, pk):
    tipo_persona = get_object_or_404(TipoPersona, pk=pk)
    if request.method == "POST":
        form = TipoPersonaForm(request.POST, instance=tipo_persona)
        if form.is_valid():
            form.save()
            return redirect('tipo_persona_list')
    else:
        form = TipoPersonaForm(instance=tipo_persona)
    return render(request, 'tipo_persona_form.html', {'form': form})

def tipo_persona_delete(request, pk):
    tipo_persona = get_object_or_404(TipoPersona, pk=pk)
    if request.method == "POST":
        tipo_persona.delete()
        return redirect('tipo_persona_list')
    return render(request, 'tipo_persona_delete.html', {'tipo_persona': tipo_persona})

def tipo_vivienda_create(request):
    if request.method == "POST":
        form = TipoViviendaForm(request.POST)
        if form.is_valid():
            tipo_vivienda = form.save(commit=False)
            tipo_vivienda.tipvivestreg = 'A'  # Asegurarse de que el estado por defecto sea 'A'
            tipo_vivienda.save()
            return redirect('tipo_vivienda_list')
    else:
        form = TipoViviendaForm()
    return render(request, 'tipo_vivienda_form.html', {'form': form})

def tipo_vivienda_update(request, pk):
    tipo_vivienda = get_object_or_404(TipoVivienda, pk=pk)
    if request.method == "POST":
        form = TipoViviendaForm(request.POST, instance=tipo_vivienda)
        if form.is_valid():
            form.save()
            return redirect('tipo_vivienda_list')
    else:
        form = TipoViviendaForm(instance=tipo_vivienda)
    return render(request, 'tipo_vivienda_form.html', {'form': form})

def tipo_vivienda_delete(request, pk):
    tipo_vivienda = get_object_or_404(TipoVivienda, pk=pk)
    if request.method == "POST":
        tipo_vivienda.delete()
        return redirect('tipo_vivienda_list')
    return render(request, 'tipo_vivienda_delete.html', {'tipo_vivienda': tipo_vivienda})

