from django.db import models
from datetime import datetime
from contabilidad.models import Moneda
from contabilidad.moneyfmt import moneyfmt


class Financiador(models.Model):
    nombre = models.CharField(max_length=600,unique=True)
    
    def __unicode__(self):
        return self.nombre
    
class Prestamo(models.Model):
    financiador = models.ForeignKey(Financiador)
    monto = models.DecimalField(max_digits=14 ,decimal_places=2)
    moneda = models.ForeignKey(Moneda)
    inicio = models.DateField(default= datetime.today())
    fin = models.DateField(blank=True, null = True)
    
    @property
    def abonado(self):
        return sum([c.monto for c in self.cuota_set.all()])
    
    @property
    def pendiente(self):
        return moneyfmt(self.monto - self.abonado,2,self.moneda.simbolo)
    
    
class Cuota(models.Model):
    fecha = models.DateField(default= datetime.today())
    monto = models.DecimalField(max_digits=14 ,decimal_places=2)
    prestamo = models.ForeignKey(Prestamo)
    

class Cuenta(models.Model):
    nombre = models.CharField(max_length=255,unique=True)
    minino = models.DecimalField(max_digits=14 ,decimal_places=2)
    moneda = models.ForeignKey(Moneda)
    
    def __unicode__(self):
        return self.nombre
    
class Deposito(models.Model):
    cuenta = models.ForeignKey(Cuenta)
    monto = models.DecimalField(max_digits=14 ,decimal_places=2)
    fecha = models.DateField(default= datetime.today())
    
    
