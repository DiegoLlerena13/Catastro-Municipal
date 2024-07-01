from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import *


# Create your views here.
def base(request):
    return render(request, 'cm/base.html')

def region_list(request):
    regiones = Region.objects.all()
    return render(request, 'region_list.html', {'regiones': regiones})

def region_create(request):
    if request.method == 'POST':
        regnom = request.POST.get('regnom')
        regestreg = request.POST.get('regestreg')
        region = Region(regnom=regnom, regestreg=regestreg)
        region.save()
        return redirect('region_list')
    return render(request, 'region_form.html')

def region_update(request, pk):
    region = get_object_or_404(Region, regcod=pk)
    if request.method == 'POST':
        regnom = request.POST.get('regnom')
        regestreg = request.POST.get('regestreg')
        region.regnom = regnom
        region.regestreg = regestreg
        region.save()
        return redirect('region_list')
    return render(request, 'region_form.html', {'region': region})

def region_delete(request, pk):
    region = get_object_or_404(Region, pk=pk)
    if request.method == "POST":
        region.delete()
        return redirect('estado_registro_list')
    return render(request, 'region_delete.html', {'region': region})



def municipio_list(request):
    municipios = Municipio.objects.all()
    return render(request, 'municipio_list.html', {'municipios': municipios})

