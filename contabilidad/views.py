# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext, Variable, defaultfilters
from django.views.generic import FormView
from django.db.models import Sum
from datetime import datetime
from settings import *
from ingresos.models import Contrato
from egresos.models import ListaCompra
from contabilidad.models import Moneda

def index(request):
    """
    Listado de reportes estadísticos
    """
    
    monedas = Moneda.objects.all()
    ingresos = Contrato.objects.values('moneda').annotate(total=Sum('monto'))
    egresos = ListaCompra.objects.values('compra__moneda').annotate(total=Sum('monto')) 
    return render_to_response('contabilidad/index.html', 
            {'ingresos':ingresos, 'egresos':egresos , 'monedas':monedas},
            context_instance=RequestContext(request))

