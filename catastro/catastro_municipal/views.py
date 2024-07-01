from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')  # Asegúrate de que tienes la plantilla index.html

def zona_urbana_view(request):
    # Tu lógica para la vista de zona urbana
    return render(request, 'catastro_municipal/zona_urbana.html')
def casa_view(request):
    # Tu lógica para la vista de casa
    return render(request, 'catastro_municipal/casa.html')
def familia_view(request):
    # Tu lógica para la vista de casa
    return render(request, 'catastro_municipal/familia.html')
def municipio_view(request):
    # Tu lógica para la vista de casa
    return render(request, 'catastro_municipal/municipio.html')
def pago_tributario_view(request):
    # Tu lógica para la vista de casa
    return render(request, 'catastro_municipal/pago_tributario.html')
def persona_view(request):
    # Tu lógica para la vista de casa
    return render(request, 'catastro_municipal/persona.html')
def propietario_view(request):
    # Tu lógica para la vista de casa
    return render(request, 'catastro_municipal/propietario.html')
def region_view(request):
    # Tu lógica para la vista de casa
    return render(request, 'catastro_municipal/region.html')
def tipo_persona_view(request):
    # Tu lógica para la vista de casa
    return render(request, 'catastro_municipal/tipo_persona.html')
def tipo_vivienda_view(request):
    # Tu lógica para la vista de casa
    return render(request, 'catastro_municipal/tipo_vivienda.html')
def vivienda_view(request):
    # Tu lógica para la vista de casa
    return render(request, 'catastro_municipal/vivienda.html')
