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
        return redirect('region_list')
    return render(request, 'region_delete.html', {'region': region})

def municipio_list(request):
    municipios = Municipio.objects.all()
    return render(request, 'municipio_list.html', {'municipios': municipios})

def municipio_create(request):
    if request.method == 'POST':
        munnom = request.POST.get('munnom')
        munpreanu = request.POST.get('munpreanu')
        munnumviv = request.POST.get('munnumviv')
        regcod = request.POST.get('regcod')
        munestreg = request.POST.get('munestreg')
        municipio = Municipio(munnom=munnom, munpreanu=munpreanu, munnumviv=munnumviv, regcod=regcod, munestreg=munestreg)
        municipio.save()
        return redirect('municipio_list')
    return render(request, 'municipio_form.html')

def municipio_update(request, pk):
    municipio = get_object_or_404(Municipio, muncod=pk)
    if request.method == 'POST':
        munnom = request.POST.get('munnom')
        munpreanu = request.POST.get('munpreanu')
        munnumviv = request.POST.get('munnumviv')
        regcod = request.POST.get('regcod')
        munestreg = request.POST.get('munestreg')
        municipio.munnom = munnom
        municipio.munpreanu = munpreanu
        municipio.munnumviv = munnumviv
        municipio.regcod = regcod
        municipio.munestreg = munestreg
        municipio.save()
        return redirect('municipio_list')
    return render(request, 'municipio_form.html', {'municipio': municipio})

def municipio_delete(request, pk):
    municipio = get_object_or_404(Municipio, pk=pk)
    if request.method == "POST":
        municipio.delete()
        return redirect('municipio_list')
    return render(request, 'municipio_delete.html', {'municipio': municipio})

def zona_urbana_list(request):
    zonas_urbanas = ZonaUrbana.objects.all()
    return render(request, 'zona_urbana_list.html', {'zonas_urbanas': zonas_urbanas})

def zona_urbana_create(request):
    if request.method == 'POST':
        zonnom = request.POST.get('zonnom')
        muncod = request.POST.get('muncod')
        zonestreg = request.POST.get('zonestreg')
        zona_urbana = ZonaUrbana(zonnom=zonnom, muncod=muncod, zonestreg=zonestreg)
        zona_urbana.save()
        return redirect('zona_urbana_list')
    return render(request, 'zona_urbana_form.html')

def zona_urbana_update(request, pk):
    zona_urbana = get_object_or_404(ZonaUrbana, zoncod=pk)
    if request.method == 'POST':
        zonnom = request.POST.get('zonnom')
        muncod = request.POST.get('muncod')
        zonestreg = request.POST.get('zonestreg')
        zona_urbana.zonnom = zonnom
        zona_urbana.muncod = muncod
        zona_urbana.zonestreg = zonestreg
        zona_urbana.save()
        return redirect('zona_urbana_list')
    return render(request, 'zona_urbana_form.html', {'zona_urbana': zona_urbana})

def zona_urbana_delete(request, pk):
    zona_urbana = get_object_or_404(ZonaUrbana, pk=pk)
    if request.method == "POST":
        zona_urbana.delete()
        return redirect('zona_urbana_list')
    return render(request, 'zona_urbana_delete.html', {'zona_urbana': zona_urbana})

def tipo_vivienda_list(request):
    tipos_vivienda = TipoVivienda.objects.all()
    return render(request, 'tipo_vivienda_list.html', {'tipos_vivienda': tipos_vivienda})

def tipo_vivienda_create(request):
    if request.method == 'POST':
        tipvivdes = request.POST.get('tipvivdes')
        tipvivestreg = request.POST.get('tipvivestreg')
        tipo_vivienda = TipoVivienda(tipvivdes=tipvivdes, tipvivestreg=tipvivestreg)
        tipo_vivienda.save()
        return redirect('tipo_vivienda_list')
    return render(request, 'tipo_vivienda_form.html')

def tipo_vivienda_update(request, pk):
    tipo_vivienda = get_object_or_404(TipoVivienda, tipvivcod=pk)
    if request.method == 'POST':
        tipvivdes = request.POST.get('tipvivdes')
        tipvivestreg = request.POST.get('tipvivestreg')
        tipo_vivienda.tipvivdes = tipvivdes
        tipo_vivienda.tipvivestreg = tipvivestreg
        tipo_vivienda.save()
        return redirect('tipo_vivienda_list')
    return render(request, 'tipo_vivienda_form.html', {'tipo_vivienda': tipo_vivienda})

def tipo_vivienda_delete(request, pk):
    tipo_vivienda = get_object_or_404(TipoVivienda, pk=pk)
    if request.method == "POST":
        tipo_vivienda.delete()
        return redirect('tipo_vivienda_list')
    return render(request, 'tipo_vivienda_delete.html', {'tipo_vivienda': tipo_vivienda})

def vivienda_list(request):
    viviendas = Vivienda.objects.all()
    return render(request, 'vivienda_list.html', {'viviendas': viviendas})

def vivienda_create(request):
    if request.method == 'POST':
        vivcal = request.POST.get('vivcal')
        vivnum = request.POST.get('vivnum')
        vivcodpos = request.POST.get('vivcodpos')
        vivocu = request.POST.get('vivocu')
        zoncod = request.POST.get('zoncod')
        tipvivcod = request.POST.get('tipvivcod')
        vivestreg = request.POST.get('vivestreg')
        vivienda = Vivienda(vivcal=vivcal, vivnum=vivnum, vivcodpos=vivcodpos, vivocu=vivocu, zoncod=zoncod, tipvivcod=tipvivcod, vivestreg=vivestreg)
        vivienda.save()
        return redirect('vivienda_list')
    return render(request, 'vivienda_form.html')

def vivienda_update(request, pk):
    vivienda = get_object_or_404(Vivienda, vivcod=pk)
    if request.method == 'POST':
        vivcal = request.POST.get('vivcal')
        vivnum = request.POST.get('vivnum')
        vivcodpos = request.POST.get('vivcodpos')
        vivocu = request.POST.get('vivocu')
        zoncod = request.POST.get('zoncod')
        tipvivcod = request.POST.get('tipvivcod')
        vivestreg = request.POST.get('vivestreg')
        vivienda.vivcal = vivcal
        vivienda.vivnum = vivnum
        vivienda.vivcodpos = vivcodpos
        vivienda.vivocu = vivocu
        vivienda.zoncod = zoncod
        vivienda.tipvivcod = tipvivcod
        vivienda.vivestreg = vivestreg
        vivienda.save()
        return redirect('vivienda_list')
    return render(request, 'vivienda_form.html', {'vivienda': vivienda})

def vivienda_delete(request, pk):
    vivienda = get_object_or_404(Vivienda, pk=pk)
    if request.method == "POST":
        vivienda.delete()
        return redirect('vivienda_list')
    return render(request, 'vivienda_delete.html', {'vivienda': vivienda})

def familia_list(request):
    familias = Familia.objects.all()
    return render(request, 'familia_list.html', {'familias': familias})

def familia_create(request):
    if request.method == 'POST':
        famnom = request.POST.get('famnom')
        famnumint = request.POST.get('famnumint')
        famestreg = request.POST.get('famestreg')
        familia = Familia(famnom=famnom, famnumint=famnumint, famestreg=famestreg)
        familia.save()
        return redirect('familia_list')
    return render(request, 'familia_form.html')

def familia_update(request, pk):
    familia = get_object_or_404(Familia, famcod=pk)
    if request.method == 'POST':
        famnom = request.POST.get('famnom')
        famnumint = request.POST.get('famnumint')
        famestreg = request.POST.get('famestreg')
        familia.famnom = famnom
        familia.famnumint = famnumint
        familia.famestreg = famestreg
        familia.save()
        return redirect('familia_list')
    return render(request, 'familia_form.html', {'familia': familia})

def familia_delete(request, pk):
    familia = get_object_or_404(Familia, pk=pk)
    if request.method == "POST":
        familia.delete()
        return redirect('familia_list')
    return render(request, 'familia_delete.html', {'familia': familia})

def tipo_persona_list(request):
    tipos_persona = TipoPersona.objects.all()
    return render(request, 'tipo_persona_list.html', {'tipos_persona': tipos_persona})

def tipo_persona_create(request):
    if request.method == 'POST':
        tipperdes = request.POST.get('tipperdes')
        tipvivestreg = request.POST.get('tipvivestreg')
        tipo_persona = TipoPersona(tipperdes=tipperdes, tipvivestreg=tipvivestreg)
        tipo_persona.save()
        return redirect('tipo_persona_list')
    return render(request, 'tipo_persona_form.html')

def tipo_persona_update(request, pk):
    tipo_persona = get_object_or_404(TipoPersona, tippercod=pk)
    if request.method == 'POST':
        tipperdes = request.POST.get('tipperdes')
        tipvivestreg = request.POST.get('tipvivestreg')
        tipo_persona.tipperdes = tipperdes
        tipo_persona.tipvivestreg = tipvivestreg
        tipo_persona.save()
        return redirect('tipo_persona_list')
    return render(request, 'tipo_persona_form.html', {'tipo_persona': tipo_persona})

def tipo_persona_delete(request, pk):
    tipo_persona = get_object_or_404(TipoPersona, pk=pk)
    if request.method == "POST":
        tipo_persona.delete()
        return redirect('tipo_persona_list')
    return render(request, 'tipo_persona_delete.html', {'tipo_persona': tipo_persona})

def persona_list(request):
    personas = Persona.objects.all()
    return render(request, 'persona_list.html', {'personas': personas})

def persona_create(request):
    if request.method == 'POST':
        pernom = request.POST.get('pernom')
        perapepat = request.POST.get('perapepat')
        perapemat = request.POST.get('perapemat')
        famcod = request.POST.get('famcod')
        tippercod = request.POST.get('tippercod')
        perestreg = request.POST.get('perestreg')
        persona = Persona(pernom=pernom, perapepat=perapepat, perapemat=perapemat, famcod=famcod, tippercod=tippercod, perestreg=perestreg)
        persona.save()
        return redirect('persona_list')
    return render(request, 'persona_form.html')

def persona_update(request, pk):
    persona = get_object_or_404(Persona, percod=pk)
    if request.method == 'POST':
        pernom = request.POST.get('pernom')
        perapepat = request.POST.get('perapepat')
        perapemat = request.POST.get('perapemat')
        famcod = request.POST.get('famcod')
        tippercod = request.POST.get('tippercod')
        perestreg = request.POST.get('perestreg')
        persona.pernom = pernom
        persona.perapepat = perapepat
        persona.perapemat = perapemat
        persona.famcod = famcod
        persona.tippercod = tippercod
        persona.perestreg = perestreg
        persona.save()
        return redirect('persona_list')
    return render(request, 'persona_form.html', {'persona': persona})

def persona_delete(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        persona.delete()
        return redirect('persona_list')
    return render(request, 'persona_delete.html', {'persona': persona})

def casa_list(request):
    casas = Casa.objects.all()
    return render(request, 'casa_list.html', {'casas': casas})

def casa_create(request):
    if request.method == 'POST':
        vivcod = request.POST.get('vivcod')
        casesc = request.POST.get('casesc')
        cascodblo = request.POST.get('cascodblo')
        caspla = request.POST.get('caspla')
        casnumpue = request.POST.get('casnumpue')
        casmet = request.POST.get('casmet')
        famcod = request.POST.get('famcod')
        casestreg = request.POST.get('casestreg')
        casocu = request.POST.get('casocu')
        casa = Casa(vivcod=vivcod, casesc=casesc, cascodblo=cascodblo, caspla=caspla, casnumpue=casnumpue, casmet=casmet, famcod=famcod, casestreg=casestreg, casocu=casocu)
        casa.save()
        return redirect('casa_list')
    return render(request, 'casa_form.html')

def casa_update(request, pk):
    casa = get_object_or_404(Casa, cascod=pk)
    if request.method == 'POST':
        vivcod = request.POST.get('vivcod')
        casesc = request.POST.get('casesc')
        cascodblo = request.POST.get('cascodblo')
        caspla = request.POST.get('caspla')
        casnumpue = request.POST.get('casnumpue')
        casmet = request.POST.get('casmet')
        famcod = request.POST.get('famcod')
        casestreg = request.POST.get('casestreg')
        casocu = request.POST.get('casocu')
        casa.vivcod = vivcod
        casa.casesc = casesc
        casa.cascodblo = cascodblo
        casa.caspla = caspla
        casa.casnumpue = casnumpue
        casa.casmet = casmet
        casa.famcod = famcod
        casa.casestreg = casestreg
        casa.casocu = casocu
        casa.save()
        return redirect('casa_list')
    return render(request, 'casa_form.html', {'casa': casa})

def casa_delete(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    if request.method == "POST":
        casa.delete()
        return redirect('casa_list')
    return render(request, 'casa_delete.html', {'casa': casa})

def propietario_list(request):
    propietarios = Propietario.objects.all()
    return render(request, 'propietario_list.html', {'propietarios': propietarios})

def propietario_create(request):
    if request.method == 'POST':
        propagtri = request.POST.get('propagtri')
        promoningfam = request.POST.get('promoningfam')
        percod = request.POST.get('percod')
        famcod = request.POST.get('famcod')
        proestreg = request.POST.get('proestreg')
        propietario = Propietario(propagtri=propagtri ,promoningfam=promoningfam, percod=percod, famcod=famcod, proestreg=proestreg)
        propietario.save()
        return redirect('propietario_list')
    return render(request, 'propietario_form.html')

def propietario_update(request, pk):
    propietario = get_object_or_404(Propietario, procod=pk)
    if request.method == 'POST':
        propagtri = request.POST.get('propagtri')
        promoningfam = request.POST.get('promoningfam')
        percod = request.POST.get('percod')
        famcod = request.POST.get('famcod')
        proestreg = request.POST.get('proestreg')
        propietario.propagtri = propagtri
        propietario.promoningfam = promoningfam
        propietario.percod = percod
        propietario.famcod = famcod
        propietario.proestreg = proestreg
        propietario.save()
        return redirect('propietario_list')
    return render(request, 'propietario_form.html', {'propietario': propietario})

def propietario_delete(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == "POST":
        propietario.delete()
        return redirect('propietario_list')
    return render(request, 'propietario_delete.html', {'propietario': propietario})

def pago_tributario_list(request):
    pagos_tributarios = PagoTributario.objects.all()
    return render(request, 'pago_tributario_list.html', {'pagos_tributarios': pagos_tributarios})

def pago_tributario_create(request):
    if request.method == 'POST':
        pagtrifec = request.POST.get('pagtrifec')
        cascod = request.POST.get('cascod')
        pagtriestreg = request.POST.get('pagtriestreg')
        pago_tributario = PagoTributario(pagtrifec=pagtrifec, cascod=cascod, pagtriestreg=pagtriestreg)
        pago_tributario.save()
        return redirect('pago_tributario_list')
    return render(request, 'pago_tributario_form.html')

def pago_tributario_update(request, pk):
    pago_tributario = get_object_or_404(PagoTributario, pagtricod=pk)
    if request.method == 'POST':
        pagtrifec = request.POST.get('pagtrifec')
        cascod = request.POST.get('cascod')
        pagtriestreg = request.POST.get('pagtriestreg')
        pago_tributario.pagtrifec = pagtrifec
        pago_tributario.cascod = cascod
        pago_tributario.pagtriestreg = pagtriestreg
        pago_tributario.save()
        return redirect('pago_tributario_list')
    return render(request, 'pago_tributario_form.html', {'pago_tributario': pago_tributario})

def pago_tributario_delete(request, pk):
    pago_tributario = get_object_or_404(PagoTributario, pk=pk)
    if request.method == "POST":
        pago_tributario.delete()
        return redirect('pago_tributario_list')
    return render(request, 'pago_tributario_delete.html', {'pago_tributario': pago_tributario})

