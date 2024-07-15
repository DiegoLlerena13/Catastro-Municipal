from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('regiones/', views.region_list, name='region_list'),
    path('municipios/', views.municipio_list, name='municipio_list'),
    path('zonas_urbanas/', views.zona_urbana_list, name='zona_urbana_list'),
    path('tipo_vivienda/', views.tipo_vivienda_list, name='tipo_vivienda_list'),
    path('viviendas/', views.vivienda_list, name='vivienda_list'),
    path('casas/', views.casa_list, name='casa_list'),
    path('familias/', views.familia_list, name='familia_list'),
    path('personas/', views.persona_list, name='persona_list'),
    path('tipo_persona/', views.tipo_persona_list, name='tipo_persona_list'),
    path('propietarios/', views.propietario_list, name='propietario_list'),
    path('pagos_tributarios/', views.pago_tributario_list, name='pago_tributario_list'),
    path('regiones/new/', views.region_create, name='region_create'),
    path('regiones/edit/<int:pk>/', views.region_update, name='region_update'),
    path('regiones/delete/<int:pk>/', views.region_delete, name='region_delete'),
    path('municipios/new/', views.municipio_create, name='municipio_create'),
    path('municipios/edit/<int:pk>/', views.municipio_update, name='municipio_update'),
    path('municipios/delete/<int:pk>/', views.municipio_delete, name='municipio_delete'),
    path('zonas_urbanas/new/', views.zona_urbana_create, name='zona_urbana_create'),
    path('zonas_urbanas/edit/<int:pk>/', views.zona_urbana_update, name='zona_urbana_update'),
    path('zonas_urbanas/delete/<int:pk>/', views.zona_urbana_delete, name='zona_urbana_delete'),
    path('viviendas/new/', views.vivienda_create, name='vivienda_create'),
    path('viviendas/edit/<int:pk>/', views.vivienda_update, name='vivienda_update'),
    path('viviendas/delete/<int:pk>/', views.vivienda_delete, name='vivienda_delete'),
    # path('casas/new/', views.casa_create, name='casa_create'),
    path('familias/new/', views.familia_create, name='familia_create'),
    path('familias/<int:pk>/edit/', views.familia_update, name='familia_update'),
    path('familias/<int:pk>/delete/', views.familia_delete, name='familia_delete'),
    path('personas/new/', views.persona_create, name='persona_create'),
    path('persona/create2/<int:fam_cod>/', views.persona_create2, name='persona_create2'),
    path('personas/<int:pk>/edit/', views.persona_update, name='persona_update'),
    path('personas/<int:pk>/delete/', views.persona_delete, name='persona_delete'),
    # path('propietarios/new/', views.propietario_create, name='propietario_create'),
    # path('pagos_tributarios/new/', views.pago_tributario_create, name='pago_tributario_create'),
    path('tipo_persona/new/', views.tipo_persona_create, name='tipo_persona_create'),
    path('tipo_persona/edit/<int:pk>/', views.tipo_persona_update, name='tipo_persona_update'),
    path('tipo_persona/delete/<int:pk>/', views.tipo_persona_delete, name='tipo_persona_delete'),
    path('tipo_vivienda/new/', views.tipo_vivienda_create, name='tipo_vivienda_create'),
    path('tipo_vivienda/edit/<int:pk>/', views.tipo_vivienda_update, name='tipo_vivienda_update'),
    path('tipo_vivienda/delete/<int:pk>/', views.tipo_vivienda_delete, name='tipo_vivienda_delete'),
    path('propietarios/new/', views.propietario_create, name='propietario_create'),
    path('propietarios/edit/<int:pk>/', views.propietario_update, name='propietario_update'),
    path('propietarios/delete/<int:pk>/', views.propietario_delete, name='propietario_delete'),
    path('casas/new/', views.casa_create, name='casa_create'),
    path('casas/edit/<int:pk>/', views.casa_update, name='casa_update'),
    path('casas/delete/<int:pk>/', views.casa_delete, name='casa_delete'),
    path('pagos_tributarios/new/', views.pago_tributario_create, name='pago_tributario_create'),
    path('pagos_tributarios/edit/<int:pk>/', views.pago_tributario_update, name='pago_tributario_update'),
    path('pagos_tributarios/delete/<int:pk>/', views.pago_tributario_delete, name='pago_tributario_delete'),
    path('', views.base, name='base'),
]