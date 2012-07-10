# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Medida'
        db.create_table('egresos_medida', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=600)),
            ('simbolo', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('egresos', ['Medida'])

        # Adding model 'Categoria'
        db.create_table('egresos_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=600)),
        ))
        db.send_create_signal('egresos', ['Categoria'])

        # Adding model 'Producto'
        db.create_table('egresos_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=600)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['egresos.Categoria'], null=True, blank=True)),
            ('medida', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['egresos.Medida'])),
        ))
        db.send_create_signal('egresos', ['Producto'])

        # Adding model 'Proveedor'
        db.create_table('egresos_proveedor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=600)),
        ))
        db.send_create_signal('egresos', ['Proveedor'])

        # Adding model 'Compra'
        db.create_table('egresos_compra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 6, 20, 16, 27, 44, 148865))),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['egresos.Proveedor'])),
        ))
        db.send_create_signal('egresos', ['Compra'])

        # Adding model 'ListaCompra'
        db.create_table('egresos_listacompra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['egresos.Compra'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['egresos.Producto'])),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('egresos', ['ListaCompra'])


    def backwards(self, orm):
        
        # Deleting model 'Medida'
        db.delete_table('egresos_medida')

        # Deleting model 'Categoria'
        db.delete_table('egresos_categoria')

        # Deleting model 'Producto'
        db.delete_table('egresos_producto')

        # Deleting model 'Proveedor'
        db.delete_table('egresos_proveedor')

        # Deleting model 'Compra'
        db.delete_table('egresos_compra')

        # Deleting model 'ListaCompra'
        db.delete_table('egresos_listacompra')


    models = {
        'egresos.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'})
        },
        'egresos.compra': {
            'Meta': {'object_name': 'Compra'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 6, 20, 16, 27, 44, 148865)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['egresos.Producto']", 'through': "orm['egresos.ListaCompra']", 'symmetrical': 'False'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['egresos.Proveedor']"})
        },
        'egresos.listacompra': {
            'Meta': {'object_name': 'ListaCompra'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'compra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['egresos.Compra']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
