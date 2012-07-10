# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import *


class ContratoAdmin(admin.ModelAdmin):
    model = Contrato
    list_display = ['servicio','cliente','monto_m','fecha']
    
admin.site.register(Servicio)
admin.site.register(Cliente)
admin.site.register(Contrato,ContratoAdmin)