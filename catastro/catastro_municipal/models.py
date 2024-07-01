from django.db import models

class ZonaUrbana(models.Model):
    codzona = models.CharField(max_length=10)
    nomzona = models.CharField(max_length=100)

class OtroModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.CharField(max_length=100)
