from django.db import models
from datetime import datetime
# Create your models here.

class Giornalista (models.Model):
    """ il modello generico di un giornalista """
    nome = models.CharField( max_length=20 )
    cognome = models.CharField( max_length=20 )
    anno_di_nascita = models.DateField(max_length=10, default=datetime.now(), blank=True)


    def __str__(self):
        return self.nome + "    " + self.cognome
    
    class Meta:
        verbose_name = "Giornalista"
        verbose_name_plural = "Giornalisti"

class Articolo (models.Model):
    """ il modello generico di un articolo di news """
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField(blank=True,null=True)
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name = "articoli")
    visualizzazioni = models.IntegerField(blank=True, default=0)
    data = models.DateField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"

