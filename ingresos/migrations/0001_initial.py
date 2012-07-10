# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Servicio'
        db.create_table('ingresos_servicio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=600)),
        ))
        db.send_create_signal('ingresos', ['Servicio'])

        # Adding model 'Cliente'
        db.create_table('ingresos_cliente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=600)),
            ('es_empresa', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('ingresos', ['Cliente'])

        # Adding model 'Contrato'
        db.create_table('ingresos_contrato', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ingresos.Servicio'])),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ingresos.Cliente'])),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 6, 20, 16, 27, 48, 98305))),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=2)),
            ('moneda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contabilidad.Moneda'])),
            ('deduccion', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=14, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('ingresos', ['Contrato'])


    def backwards(self, orm):
        
        # Deleting model 'Servicio'
        db.delete_table('ingresos_servicio')

        # Deleting model 'Cliente'
        db.delete_table('ingresos_cliente')

        # Deleting model 'Contrato'
        db.delete_table('ingresos_contrato')


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
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 6, 20, 16, 27, 48, 98305)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contabilidad.Moneda']"}),
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
