from django.db import models
from django.core.exceptions import ValidationError
class Region(models.Model):
    regcod = models.AutoField(db_column='RegCod', primary_key=True, verbose_name="Código")
    regnom = models.CharField(db_column='RegNom', max_length=20, verbose_name="Nombre")
    regestreg = models.CharField(db_column='RegEstReg', max_length=1, default='A', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
        db_table = 'region'

    def _str_(self):
        return self.regnom

class Municipio(models.Model):
    muncod = models.AutoField(db_column='MunCod', primary_key=True, verbose_name="Código")
    munnom = models.CharField(db_column='MunNom', max_length=20, verbose_name="Nombre")
    munpreanu = models.DecimalField(db_column='MunPreAnu', max_digits=8, decimal_places=0, verbose_name="Presupuesto Anual")
    munnumviv = models.IntegerField(db_column='MunNumViv', verbose_name="Número de Viviendas")
    regcod = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='RegCod', verbose_name="Código de Región")
    munestreg = models.CharField(db_column='MunEstReg', max_length=1, default='A', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        db_table = 'municipio'

    def _str_(self):
        return self.munnom

class ZonaUrbana(models.Model):
    zoncod = models.AutoField(db_column='ZonCod', primary_key=True, verbose_name="Código")
    zonnom = models.CharField(db_column='ZonNom', max_length=20, verbose_name="Nombre")
    muncod = models.ForeignKey(Municipio, on_delete=models.CASCADE, db_column='MunCod', verbose_name="Código de Municipio")
    zonestreg = models.CharField(db_column='ZonEstReg', max_length=1, default='A', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Zona Urbana"
        verbose_name_plural = "Zonas Urbanas"
        db_table = 'zona_urbana'

    def _str_(self):
        return self.zonnom

class TipoVivienda(models.Model):
    tipvivcod = models.AutoField(db_column='TipVivCod', primary_key=True, verbose_name="Código")
    tipvivdes = models.CharField(db_column='TipVivDes', max_length=15, verbose_name="Descripción")
    tipvivestreg = models.CharField(db_column='TipVivEstReg', max_length=1, default='A', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Tipo de Vivienda"
        verbose_name_plural = "Tipos de Vivienda"
        db_table = 'tipo_vivienda'

    def _str_(self):
        return self.tipvivdes

class Vivienda(models.Model):
    vivcod = models.AutoField(db_column='VivCod', primary_key=True, verbose_name="Código")
    vivcal = models.CharField(db_column='VivCal', max_length=3, verbose_name="Calle")
    vivnum = models.IntegerField(db_column='VivNum', verbose_name="Número")
    vivcodpos = models.IntegerField(db_column='VivCodPos', verbose_name="Código Postal")
    vivmet = models.DecimalField(db_column='VivMet', max_digits=4, decimal_places=0, verbose_name="Metros")
    vivocu = models.CharField(db_column='VivOcu', max_length=1, verbose_name="Ocupación")
    zoncod = models.ForeignKey(ZonaUrbana, on_delete=models.CASCADE, db_column='ZonCod', verbose_name="Código de Zona")
    tipvivcod = models.ForeignKey(TipoVivienda, on_delete=models.CASCADE, db_column='TipVivCod', verbose_name="Código de Tipo de Vivienda")
    vivestreg = models.CharField(db_column='VivEstReg', max_length=1, default='A', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Vivienda"
        verbose_name_plural = "Viviendas"
        db_table = 'vivienda'

    def _str_(self):
        return f"Vivienda {self.vivcod}"

class Familia(models.Model):
    famcod = models.AutoField(db_column='FamCod', primary_key=True, verbose_name="Código")
    famnom = models.CharField(db_column='FamNom', max_length=15, verbose_name="Nombre")
    famnumint = models.IntegerField(db_column='FamNumInt', verbose_name="Número de Integrantes")
    famestreg = models.CharField(db_column='FamEstReg', max_length=1, default='A', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familias"
        db_table = 'familia'

    def _str_(self):
        return self.famnom

class TipoPersona(models.Model):
    tippercod = models.AutoField(db_column='TipPerCod', primary_key=True, verbose_name="Código")
    tipperdes = models.CharField(db_column='TipPerDes', max_length=15, verbose_name="Descripción")
    tipvivestreg = models.CharField(db_column='TipVivEstReg', max_length=1, verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Tipo de Persona"
        verbose_name_plural = "Tipos de Persona"
        db_table = 'tipo_persona'

    def _str_(self):
        return self.tipperdes

class Persona(models.Model):
    percod = models.AutoField(db_column='PerCod', primary_key=True, verbose_name="Código")
    pernom = models.CharField(db_column='PerNom', max_length=15, verbose_name="Nombre")
    perapepat = models.CharField(db_column='PerApePat', max_length=10, verbose_name="Apellido Paterno")
    perapemat = models.CharField(db_column='PerApeMat', max_length=10, verbose_name="Apellido Materno")
    famcod = models.ForeignKey(Familia, on_delete=models.CASCADE, db_column='FamCod', verbose_name="Código de Familia")
    tippercod = models.ForeignKey(TipoPersona, on_delete=models.CASCADE, db_column='TipPerCod', verbose_name="Código de Tipo de Persona")
    perestreg = models.CharField(db_column='PerEstReg', max_length=1, verbose_name="Estado de Registro", default='A', editable=False)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        db_table = 'persona'

    def _str_(self):
        return f"{self.pernom} {self.perapepat} {self.perapemat}"

    def clean(self):
        # Verificar cantidad de integrantes de la familia
        integrantes_actuales = Persona.objects.filter(famcod=self.famcod).count()
        num_integrantes_familia = self.famcod.famnumint  # Obtener el número máximo de integrantes de la familia

        if integrantes_actuales >= num_integrantes_familia:
            raise ValidationError(f"La familia ya tiene registrados {num_integrantes_familia} integrantes. No se pueden agregar más.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Realizar la validación antes de guardar
        super().save(*args, **kwargs)

class Casa(models.Model):
    cascod = models.AutoField(db_column='CasCod', primary_key=True, verbose_name="Código")
    casesc = models.IntegerField(db_column='CasEsc', verbose_name="Escalera")
    cascodblo = models.CharField(db_column='CasCodBlo', max_length=1, verbose_name="Bloque")
    caspla = models.IntegerField(db_column='CasPla', verbose_name="Planta")
    casnumpue = models.IntegerField(db_column='CasNumPue', verbose_name="Número de Puertas")
    casmet = models.DecimalField(db_column='CasMet', max_digits=5, decimal_places=0, verbose_name="Metros")
    vivcod = models.ForeignKey(Vivienda, on_delete=models.CASCADE, db_column='VivCod', verbose_name="Código de Vivienda")
    famcod = models.ForeignKey(Familia, on_delete=models.CASCADE, db_column='FamCod', verbose_name="Código de Familia")
    casestreg = models.CharField(db_column='CasEstReg', max_length=1, default='A', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Casas"
        db_table = 'casa'

    def _str_(self):
        return f"Casa {self.cascod}"

class PagoTributario(models.Model):
    pagtricod = models.AutoField(db_column='PagTriCod', primary_key=True, verbose_name="Código")
    pagtrifec = models.DateField(db_column='PagTriFec', verbose_name="Fecha")
    cascod = models.ForeignKey(Casa, on_delete=models.CASCADE, db_column='CasCod', verbose_name="Código de Casa")
    pagtriestreg = models.CharField(db_column='PagTriEstReg', max_length=1, default='A', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Pago Tributario"
        verbose_name_plural = "Pagos Tributarios"
        db_table = 'pago_tributario'

    def _str_(self):
        return f"Pago {self.pagtricod}"

class Propietario(models.Model):
    procod = models.AutoField(db_column='ProCod', primary_key=True, verbose_name="Código")
    propagtri = models.DecimalField(db_column='ProPagTri', max_digits=8, decimal_places=0, verbose_name="Pago Tributario")
    promoningfam = models.DecimalField(db_column='ProMonIngFam', max_digits=8, decimal_places=0, verbose_name="Ingresos Familiares")
    percod = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='PerCod', verbose_name="Código de Persona")
    famcod = models.ForeignKey(Familia, on_delete=models.CASCADE, db_column='FamCod', verbose_name="Código de Familia")
    proestreg = models.CharField(db_column='ProEstReg', max_length=1, verbose_name="Estado de Registro", default='A', editable=False)

    class Meta:
        verbose_name = "Propietario"
        verbose_name_plural = "Propietarios"
        db_table = 'propietario'

    def _str_(self):
        return f"Propietario {self.procod}"

    def clean(self):
        # Verificar si el tipo de persona es "propietario"
        if self.percod.tippercod.tipperdes != 'Propietario':
            raise ValidationError('La persona no tiene el tipo "propietario" para ser registrado como propietario.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Realizar la validación antes de guardar
        if not self.procod:  # Nuevo objeto
            self.propagtri = self.promoningfam * 0.1  # Ejemplo: 10% del ingreso familiar
        super().save(*args, **kwargs)