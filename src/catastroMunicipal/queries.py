from .models import *

# Consulta para obtener todos los pagos tributarios de un propietario específico
def pagos_tributarios_por_vivienda(vivienda_id):
    try:
        casas = Casa.objects.filter(VivCod=vivienda_id)
        pagos_tributarios = PagoTributario.objects.filter(CasCod__in=casas)

        total_pagado = pagos_tributarios.aggregate(Sum('PagTriPag'))['PagTriPag__sum'] or 0
        total_pagos = pagos_tributarios.count()

        return {
            'total_pagado': total_pagado,
            'total_pagos': total_pagos
        }
    except Exception as e:
        print(f"Error al generar el reporte de pagos por vivienda: {e}")
        return None

def pagos_tributarios_por_zona(zona_id):
    try:
        viviendas = Vivienda.objects.filter(ZonCod=zona_id)
        casas = Casa.objects.filter(VivCod__in=viviendas)
        pagos_tributarios = PagoTributario.objects.filter(CasCod__in=casas)

        total_pagado = pagos_tributarios.aggregate(Sum('PagTriPag'))['PagTriPag__sum'] or 0
        total_pagos = pagos_tributarios.count()

        return {
            'total_pagado': total_pagado,
            'total_pagos': total_pagos
        }
    except Exception as e:
        print(f"Error al generar el reporte de pagos por zona: {e}")
        return None


# Consulta para obtener los pagos tributarios de un municipio específico
def pagos_tributarios_por_municipio(municipio_id):
    try:
        zonas = ZonaUrbana.objects.filter(MunCod=municipio_id)
        viviendas = Vivienda.objects.filter(ZonCod__in=zonas)
        casas = Casa.objects.filter(VivCod__in=viviendas)
        pagos_tributarios = PagoTributario.objects.filter(CasCod__in=casas)

        total_pagado = pagos_tributarios.aggregate(Sum('PagTriPag'))['PagTriPag__sum'] or 0
        total_pagos = pagos_tributarios.count()

        return {
            'total_pagado': total_pagado,
            'total_pagos': total_pagos
        }
    except Exception as e:
        print(f"Error al generar el reporte de pagos por municipio: {e}")
        return None


def pagos_tributarios_por_region(region_id):
    try:
        # Obtener todos los municipios de la región
        municipios = Municipio.objects.filter(RegCod=region_id)
        
        # Obtener todas las zonas urbanas de los municipios
        zonas = ZonaUrbana.objects.filter(MunCod__in=municipios)
        
        # Obtener todas las viviendas de las zonas urbanas
        viviendas = Vivienda.objects.filter(ZonCod__in=zonas)
        
        # Obtener todas las casas de las viviendas
        casas = Casa.objects.filter(VivCod__in=viviendas)
        
        # Obtener todos los pagos tributarios de las casas
        pagos_tributarios = PagoTributario.objects.filter(CasCod__in=casas)

        # Calcular el monto total pagado por región
        total_pagado = pagos_tributarios.aggregate(Sum('PagTriPag'))['PagTriPag__sum'] or 0
        
        # Calcular el número de pagos realizados
        total_pagos = pagos_tributarios.count()
        
        return {
            'total_pagado': total_pagado,
            'total_pagos': total_pagos
        }
    except Exception as e:
        print(f"Error al generar el reporte de pagos por región: {e}")
        return None

