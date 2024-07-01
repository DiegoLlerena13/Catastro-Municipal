from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Definir la URL para la página de inicio
    path('zona_urbana/', views.zona_urbana_view, name='zona_urbana'),
    path('casa/', views.casa_view, name='casa'),
    path('familia/', views.familia_view, name='familia'),
    path('municipio/', views.municipio_view, name='municipio'),
    path('pago_tributario/', views.pago_tributario_view, name='pago_tributario'),
    path('persona/', views.persona_view, name='persona'),
    path('propietario/', views.propietario_view, name='propietario'),
    path('region/', views.region_view, name='region'),
    path('tipo_persona/', views.tipo_persona_view, name='tipo_persona'),
    path('tipo_vivienda/', views.tipo_vivienda_view, name='tipo_vivienda'),
    path('vivienda/', views.vivienda_view, name='vivienda'),
    # Otras rutas aquí...
]
