from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('regiones/', views.region_list, name='region_list'),
    path('municipios/', views.municipio_list, name='municipio_list'),
    path('zonas_urbanas/', views.zona_urbana_list, name='zona_urbana_list'),
    path('tipos_vivienda/', views.tipo_vivienda_list, name='tipo_vivienda_list'),
    path('viviendas/', views.vivienda_list, name='vivienda_list'),
    path('casas/', views.casa_list, name='casa_list'),
    path('familias/', views.familia_list, name='familia_list'),
    path('personas/', views.persona_list, name='persona_list'),
    path('tipo_persona/', views.tipo_persona_list, name='tipo_persona_list'),
    path('propietarios/', views.propietario_list, name='propietario_list'),
    path('pagos_tributarios/', views.pago_tributario_list, name='pago_tributario_list'),
    # path('regiones/new/', views.region_create, name='region_create'),
    # path('municipios/new/', views.municipio_create, name='municipio_create'),
    # path('zonas_urbanas/new/', views.zona_urbana_create, name='zona_urbana_create'),
    # path('tipos_vivienda/new/', views.tipo_vivienda_create, name='tipo_vivienda_create'),
    # path('viviendas/new/', views.vivienda_create, name='vivienda_create'),
    # path('casas/new/', views.casa_create, name='casa_create'),
    # path('familias/new/', views.familia_create, name='familia_create'),
    # path('personas/new/', views.persona_create, name='persona_create'),
    # path('tipo_persona/new/', views.tipo_persona_create, name='tipo_persona_create'),
    # path('propietarios/new/', views.propietario_create, name='propietario_create'),
    # path('pagos_tributarios/new/', views.pago_tributario_create, name='pago_tributario_create'),
    path('', views.base, name='base'),
]