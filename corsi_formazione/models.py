from django.db import models
from datetime import datetime


class Corso (models.Model):
    titolo = models.CharField( max_length=40 )
    descrizione = models.TextField( max_length=30 )
    data_inizio = models.DateField(max_length=20, default=datetime.now(), blank=True)
    data_fine = models.DateField(max_length=20, default=datetime.now(), blank=True)
    posti_disponibili = models.IntegerField(max_length=10, default=datetime.now(), blank=True)

class Meta:
        verbose_name = "Corso"
        verbose_name_plural = "Corsi"