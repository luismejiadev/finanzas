from django.db import models
from datetime import datetime
from contabilidad.moneyfmt import moneyfmt
from contabilidad.models import Moneda

class Medida(models.Model):
    nombre = models.CharField(max_length=600,unique=True)
    simbolo = models.CharField(max_length=6)

    def __unicode__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=600, unique=True)
    
    def __unicode__(self):
        return self.nombre    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=600,unique=True)
    categoria = models.ForeignKey(Categoria,blank=True,null=True)
    medida = models.ForeignKey(Medida)
    
    

    def __unicode__(self):
        return '%s (%s)'%(self.nombre,self.medida.simbolo) 
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=600,unique=True)
    
    def __unicode__(self):
        return self.nombre    
    
class Compra(models.Model):
    fecha = models.DateField(default = datetime.today() )
    proveedor = models.ForeignKey(Proveedor)
    productos = models.ManyToManyField(Producto,through='ListaCompra')
    moneda = models.ForeignKey(Moneda, blank=True,null=True)

    def __unicode__(self):
        return format(self.fecha,"%d - %B - %Y")
    
    @property
    def _total(self):
        return sum([ p._total for p in self.listacompra_set.all()])
    
    @property
    def total(self):
        return moneyfmt(self._total,2,self.moneda.simbolo)

class ListaCompra(models.Model):
    compra = models.ForeignKey(Compra)
    producto = models.ForeignKey(Producto)
    precio = models.DecimalField(max_digits=6 ,decimal_places=2)
    cantidad = models.IntegerField( default = 1)
    monto = models.DecimalField(max_digits=6 ,decimal_places=2,default = 0)
    
    def save(self, force_insert=False, force_update=False, using=None):
        monto = self.precio * self.cantidad
        super(ListaCompra,self).save( force_insert=False, force_update=False, using=None)
    
    @property
    def _total(self):
        return self.cantidad * self.precio
    
    @property
    def total(self):
        return moneyfmt(self._total,2,'C$')        