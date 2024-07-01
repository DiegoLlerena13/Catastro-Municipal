from django.shortcuts import render, redirect
from .forms import ZonaUrbanaForm, OtroModeloForm

def gestion_view(request):
    if request.method == 'POST':
        zona_form = ZonaUrbanaForm(request.POST, prefix='zona')
        otro_form = OtroModeloForm(request.POST, prefix='otro')

        if zona_form.is_valid() and otro_form.is_valid():
            zona_form.save()
            otro_form.save()
            return redirect('gestion_view')
    else:
        zona_form = ZonaUrbanaForm(prefix='zona')
        otro_form = OtroModeloForm(prefix='otro')

    return render(request, 'catastro_municipal/gestion_template.html', {
        'zona_form': zona_form,
        'otro_form': otro_form
    })
