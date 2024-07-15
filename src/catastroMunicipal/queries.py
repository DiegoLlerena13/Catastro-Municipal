from .models import Propietario, ZonaUrbana, Municipio, PagoTributario

# Consulta para obtener todos los pagos tributarios de un propietario específico
def pagos_tributarios_por_propietario(propietario_id):
    propietario = Propietario.objects.get(pk=propietario_id)
    pagos_tributarios = PagoTributario.objects.filter(CasCod__FamCod=propietario.PerCod.FamCod)
    return pagos_tributarios

# Consulta para obtener los pagos tributarios de una zona urbana específica
def pagos_tributarios_por_zona(zona_id):
    zona_urbana = ZonaUrbana.objects.get(pk=zona_id)
    pagos_tributarios = PagoTributario.objects.filter(CasCod__ZonCod=zona_urbana)
    return pagos_tributarios

# Consulta para obtener los pagos tributarios de un municipio específico
def pagos_tributarios_por_municipio(municipio_id):
    municipio = Municipio.objects.get(pk=municipio_id)
    pagos_tributarios = PagoTributario.objects.filter(CasCod__ZonCod__MunCod=municipio)
    return pagos_tributarios