# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Contrato.moneda'
        db.add_column('ingresos_contrato', 'moneda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contabilidad.Moneda'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Contrato.moneda'
        db.delete_column('ingresos_contrato', 'moneda_id')


    models = {
        'contabilidad.moneda': {
            'Meta': {'object_name': 'Moneda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'}),
            'simbolo': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'ingresos.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'es_empresa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'})
        },
        'ingresos.contrato': {
            'Meta': {'object_name': 'Contrato'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.Cliente']"}),
            'deduccion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 6, 20, 16, 30, 22, 961348)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contabilidad.Moneda']", 'null': 'True', 'blank': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ingresos.Servicio']"})
        },
        'ingresos.servicio': {
            'Meta': {'object_name': 'Servicio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'})
        }
    }

    complete_apps = ['ingresos']
