from django.db import models
from datetime import datetime
from contabilidad.models import Moneda


class Servicio(models.Model):
    nombre = models.CharField(max_length=600,unique=True)    
    def __unicode__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=600,unique=True)
    es_empresa = models.BooleanField(default=False)
        
    def __unicode__(self):
        return self.nombre    

class Contrato(models.Model):
    servicio = models.ForeignKey(Servicio)
    cliente = models.ForeignKey(Cliente)
    fecha = models.DateField(default= datetime.today())
    monto = models.DecimalField(max_digits=14 ,decimal_places=2)
    moneda = models.ForeignKey(Moneda, blank=True,null=True)
    deduccion = models.DecimalField(max_digits=14 ,decimal_places=2, blank = True,null = True) 

    def __unicode__(self):
        return self.servicio.nombre
    
    @property
    def total(self):
        return self.monto - (self.deduccion if self.deduccion is not None else 0)
    
    @property
    def monto_m(self):
        return '%s %s'% (self.moneda.simbolo,self.total)     
    