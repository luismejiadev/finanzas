# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ListaCompra.monto'
        db.add_column('egresos_listacompra', 'monto', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=2), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ListaCompra.monto'
        db.delete_column('egresos_listacompra', 'monto')


    models = {
        'contabilidad.moneda': {
            'Meta': {'object_name': 'Moneda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'}),
            'simbolo': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'egresos.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'})
        },
        'egresos.compra': {
            'Meta': {'object_name': 'Compra'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 6, 20, 18, 30, 6, 617589)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contabilidad.Moneda']", 'null': 'True', 'blank': 'True'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['egresos.Producto']", 'through': "orm['egresos.ListaCompra']", 'symmetrical': 'False'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['egresos.Proveedor']"})
        },
        'egresos.listacompra': {
            'Meta': {'object_name': 'ListaCompra'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'compra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['egresos.Compra']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['egresos.Producto']"})
        },
        'egresos.medida': {
            'Meta': {'object_name': 'Medida'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'}),
            'simbolo': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'egresos.producto': {
            'Meta': {'object_name': 'Producto'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['egresos.Categoria']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medida': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['egresos.Medida']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'})
        },
        'egresos.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'})
        }
    }

    complete_apps = ['egresos']
