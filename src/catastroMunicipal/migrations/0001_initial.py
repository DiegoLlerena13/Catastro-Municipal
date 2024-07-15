
# Generated by Django 4.2.3 on 2024-07-15 01:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('FamCod', models.AutoField(db_column='FamCod', primary_key=True, serialize=False, verbose_name='Código')),
                ('FamNom', models.CharField(db_column='FamNom', max_length=15, verbose_name='Nombre')),
                ('FamNumInt', models.IntegerField(db_column='FamNumInt', default=0, verbose_name='Número de Integrantes')),
                ('FamEstReg', models.CharField(db_column='FamEstReg', default='A', max_length=1, verbose_name='Estado de Registro')),
            ],
            options={
                'db_table': 'Familia',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('MunCod', models.AutoField(db_column='MunCod', primary_key=True, serialize=False, verbose_name='Código')),
                ('MunNom', models.CharField(db_column='MunNom', max_length=20, unique=True, verbose_name='Nombre')),
                ('MunPreAnu', models.DecimalField(db_column='MunPreAnu', decimal_places=2, default=0, max_digits=8, verbose_name='Presupuesto Anual')),
                ('MunNumViv', models.IntegerField(db_column='MunNumViv', default=0, null=True, verbose_name='Número de Viviendas')),
                ('MunEstReg', models.CharField(db_column='MunEstReg', default='A', max_length=1, verbose_name='Estado de Registro')),
            ],
            options={
                'db_table': 'Municipio',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('PerCod', models.AutoField(db_column='PerCod', primary_key=True, serialize=False, verbose_name='Código')),
                ('PerNom', models.CharField(db_column='PerNom', max_length=20, verbose_name='Nombres')),
                ('PerEstReg', models.CharField(db_column='PerEstReg', default='A', max_length=1, verbose_name='Estado de Registro')),
                ('FamCod', models.ForeignKey(db_column='FamCod', on_delete=django.db.models.deletion.CASCADE, to='catastroMunicipal.familia', verbose_name='Código de Familia')),
            ],
            options={
                'db_table': 'Persona',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('RegCod', models.AutoField(db_column='RegCod', primary_key=True, serialize=False, verbose_name='Código')),
                ('RegNom', models.CharField(db_column='RegNom', max_length=20, unique=True, verbose_name='Nombre')),
                ('RegEstReg', models.CharField(db_column='RegEstReg', default='A', max_length=1, verbose_name='Estado de Registro')),
            ],
            options={
                'db_table': 'Region',
            },
        ),
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('TipPerCod', models.AutoField(db_column='TipPerCod', primary_key=True, serialize=False, verbose_name='Código')),
                ('TipPerDes', models.CharField(db_column='TipPerDes', max_length=15, unique=True, verbose_name='Descripción')),
                ('TipPerEstReg', models.CharField(db_column='TipPerEstReg', default='A', max_length=1, verbose_name='Estado de Registro')),
            ],
            options={
                'db_table': 'Tipo_Persona',
            },
        ),
        migrations.CreateModel(
            name='TipoVivienda',
            fields=[
                ('TipVivCod', models.AutoField(db_column='TipVivCod', primary_key=True, serialize=False, verbose_name='Código')),
                ('TipVivDes', models.CharField(db_column='TipVivDes', max_length=15, unique=True, verbose_name='Descripción')),
                ('TipVivEstReg', models.CharField(db_column='TipVivEstReg', default='A', max_length=1, verbose_name='Estado de Registro')),
            ],
            options={
                'db_table': 'Tipo_Vivienda',
            },
        ),
        migrations.CreateModel(
            name='ZonaUrbana',
            fields=[
                ('ZonCod', models.AutoField(db_column='ZonCod', primary_key=True, serialize=False, verbose_name='Código')),
                ('ZonNom', models.CharField(db_column='ZonNom', max_length=20, unique=True, verbose_name='Nombre')),
                ('ZonEstReg', models.CharField(db_column='ZonEstReg', default='A', max_length=1, verbose_name='Estado de Registro')),
                ('MunCod', models.ForeignKey(db_column='MunCod', on_delete=django.db.models.deletion.CASCADE, to='catastroMunicipal.municipio', verbose_name='Código de Municipio')),
            ],
            options={
                'db_table': 'Zona_Urbana',
            },
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('VivCod', models.AutoField(db_column='VivCod', primary_key=True, serialize=False, verbose_name='Código')),
                ('VivCal', models.CharField(db_column='VivCal', max_length=3, validators=[django.core.validators.MaxLengthValidator(3)], verbose_name='Calle')),
                ('VivNum', models.CharField(db_column='VivNum', max_length=2, validators=[django.core.validators.MaxLengthValidator(2)], verbose_name='Número')),
                ('VivCodPos', models.CharField(db_column='VivCodPos', max_length=4, validators=[django.core.validators.MaxLengthValidator(4)], verbose_name='Código Postal')),
                ('VivOcu', models.CharField(choices=[('S', 'Sí'), ('N', 'No')], db_column='VivOcu', default='N', max_length=1, verbose_name='Ocupada')),
                ('VivEstReg', models.CharField(db_column='VivEstReg', default='A', max_length=1, verbose_name='Estado de Registro')),
                ('TipVivCod', models.ForeignKey(db_column='TipVivCod', on_delete=django.db.models.deletion.CASCADE, to='catastroMunicipal.tipovivienda', verbose_name='Código de Tipo de Vivienda')),
                ('ZonCod', models.ForeignKey(db_column='ZonCod', on_delete=django.db.models.deletion.CASCADE, to='catastroMunicipal.zonaurbana', verbose_name='Código de Zona')),
            ],
            options={
                'db_table': 'Vivienda',
                'unique_together': {('VivCal', 'VivNum')},
            },
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('ProCod', models.AutoField(db_column='ProCod', primary_key=True, serialize=False, verbose_name='Código')),
                ('ProMonIngFam', models.DecimalField(db_column='ProMonIngFam', decimal_places=2, default=0, max_digits=10, verbose_name='Monto Ingreso Familiar')),
                ('ProEstReg', models.CharField(db_column='ProEstReg', default='A', max_length=1, verbose_name='Estado de Registro')),
                ('PerCod', models.ForeignKey(db_column='PerCod', on_delete=django.db.models.deletion.CASCADE, to='catastroMunicipal.persona', verbose_name='Código de Persona')),
            ],
            options={
                'db_table': 'Propietario',
            },
        ),
        migrations.AddField(
            model_name='persona',
            name='TipPerCod',
            field=models.ForeignKey(db_column='TipPerCod', on_delete=django.db.models.deletion.CASCADE, to='catastroMunicipal.tipopersona', verbose_name='Tipo Persona Código'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='RegCod',
            field=models.ForeignKey(db_column='RegCod', on_delete=django.db.models.deletion.CASCADE, to='catastroMunicipal.region', verbose_name='Código de Región'),
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('CasCod', models.AutoField(db_column='CasCod', primary_key=True, serialize=False, verbose_name='Código')),
                ('CasEsc', models.CharField(blank=True, db_column='CasEsc', default='  ', max_length=2, null=True, validators=[django.core.validators.MaxLengthValidator(2), django.core.validators.RegexValidator('^[0-9]*$', 'Ingrese solo números válidos.')], verbose_name='Escalera')),
                ('CasCodBlo', models.CharField(blank=True, db_column='CasCodBlo', default=' ', max_length=2, null=True, validators=[django.core.validators.MaxLengthValidator(2)], verbose_name='Código de Bloque')),
                ('CasPla', models.CharField(blank=True, db_column='CasPla', default='  ', max_length=2, null=True, validators=[django.core.validators.MaxLengthValidator(2), django.core.validators.RegexValidator('^[0-9]*$', 'Ingrese solo números válidos.')], verbose_name='Planta')),
                ('CasNumPue', models.CharField(blank=True, db_column='CasNumPue', default='  ', max_length=2, null=True, validators=[django.core.validators.MaxLengthValidator(2), django.core.validators.RegexValidator('^[0-9]*$', 'Ingrese solo números válidos.')], verbose_name='Número de Puerta')),
                ('CasMet', models.DecimalField(db_column='CasMet', decimal_places=2, max_digits=7, verbose_name='Metros')),
                ('CasEstReg', models.CharField(db_column='CasEstReg', default='A', max_length=1, verbose_name='Estado de Registro')),
                ('CasOcu', models.CharField(choices=[('S', 'Sí'), ('N', 'No')], db_column='CasOcu', default='N', max_length=1, verbose_name='¿Está ocupada?')),
                ('FamCod', models.ForeignKey(db_column='FamCod', on_delete=django.db.models.deletion.CASCADE, to='catastroMunicipal.familia', verbose_name='Código de Familia')),
                ('VivCod', models.ForeignKey(db_column='VivCod', on_delete=django.db.models.deletion.CASCADE, to='catastroMunicipal.vivienda', verbose_name='Código de Vivienda')),
            ],
            options={
                'db_table': 'Casa',
                'unique_together': {('CasEsc', 'CasCodBlo', 'CasPla', 'CasNumPue')},
            },
        ),
        migrations.CreateModel(
            name='PagoTributario',
            fields=[
                ('PagTriCod', models.AutoField(db_column='PagTriCod', primary_key=True, serialize=False, verbose_name='Pago Tributario Codigo')),
                ('PagTriFec', models.DateField(db_column='PagTriFec', default=django.utils.timezone.now, verbose_name='Pago Tributario Fecha emitida')),
                ('PagTriIngFam', models.DecimalField(db_column='PagTriIngFam', decimal_places=2, default=0, max_digits=6, verbose_name='Ingreso Familiar')),
                ('PagTriCat', models.CharField(db_column='PagTriCat', default=' ', max_length=1, null=True, verbose_name='Categoria')),
                ('PagTriPag', models.DecimalField(db_column='PagTriPag', decimal_places=2, default=0, max_digits=8, verbose_name='Pago Total')),
                ('PagTriEstReg', models.CharField(choices=[('en proceso', 'En Proceso'), ('pagada', 'Pagada'), ('debe', 'Debe')], db_column='PagTriEstReg', default='debe', max_length=15, verbose_name='Estado de Pago')),
                ('CasCod', models.ForeignKey(db_column='CasCod', on_delete=django.db.models.deletion.CASCADE, to='catastroMunicipal.casa', verbose_name='Código de Casa')),
            ],
            options={
                'db_table': 'Pago_Tributario',
                'unique_together': {('CasCod',)},
            },
        ),
    ]
