from django.db import models




class Moneda(models.Model):
    nombre = models.CharField(max_length=600,unique=True)
    simbolo = models.CharField(max_length=6)    
    def __unicode__(self):
        return self.nombre