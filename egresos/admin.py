# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import *

class ListaCompraLine( admin.TabularInline):
    model = ListaCompra 
    readonly_fields = ['total']
    fields = ('producto','precio','cantidad','total')
    
class CompraAdmin(admin.ModelAdmin):
    model = Compra
    inlines = [ListaCompraLine]
    readonly_fields = ['total']
    fields = ('fecha','proveedor','total')
    list_display = ('fecha','proveedor','total')
    
    
admin.site.register(Compra,CompraAdmin)
admin.site.register(Medida)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Proveedor)