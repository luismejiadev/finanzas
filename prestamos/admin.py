# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import *

class CuotaLine( admin.TabularInline):
    model = Cuota 
    
class PrestamoAdmin(admin.ModelAdmin):
    model = Prestamo
    inlines = [CuotaLine]
    list_display = ['financiador','monto','abonado','pendiente']
    

class DepositoLine( admin.TabularInline):
    model = Deposito 
    
class CuentaAdmin(admin.ModelAdmin):
    model = Cuenta
    inlines = [DepositoLine]
        
admin.site.register(Prestamo,PrestamoAdmin)
admin.site.register(Cuenta,CuentaAdmin)
admin.site.register(Moneda)
admin.site.register(Financiador)