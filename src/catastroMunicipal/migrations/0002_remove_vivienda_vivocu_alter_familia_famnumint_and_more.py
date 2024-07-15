# Generated by Django 4.2.3 on 2024-07-15 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catastroMunicipal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vivienda',
            name='VivOcu',
        ),
        migrations.AlterField(
            model_name='familia',
            name='FamNumInt',
            field=models.IntegerField(db_column='FamNumInt', null=True, verbose_name='Número de Integrantes'),
        ),
        migrations.AlterField(
            model_name='pagotributario',
            name='PagTriCat',
            field=models.CharField(db_column='PagTriCat', default='A', max_length=1, null=True, verbose_name='Categoria'),
        ),
    ]
