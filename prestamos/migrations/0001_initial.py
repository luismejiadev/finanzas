# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Financiador'
        db.create_table('prestamos_financiador', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=600)),
        ))
        db.send_create_signal('prestamos', ['Financiador'])

        # Adding model 'Prestamo'
        db.create_table('prestamos_prestamo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('financiador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prestamos.Financiador'])),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=2)),
            ('moneda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contabilidad.Moneda'])),
            ('inicio', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 6, 20, 16, 27, 55, 934235))),
            ('fin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('prestamos', ['Prestamo'])

        # Adding model 'Cuota'
        db.create_table('prestamos_cuota', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 6, 20, 16, 27, 55, 935059))),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=2)),
            ('prestamo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prestamos.Prestamo'])),
        ))
        db.send_create_signal('prestamos', ['Cuota'])

        # Adding model 'Cuenta'
        db.create_table('prestamos_cuenta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=600)),
            ('minino', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=2)),
            ('moneda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contabilidad.Moneda'])),
        ))
        db.send_create_signal('prestamos', ['Cuenta'])

        # Adding model 'Deposito'
        db.create_table('prestamos_deposito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cuenta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prestamos.Cuenta'])),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=2)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 6, 20, 16, 27, 55, 936657))),
        ))
        db.send_create_signal('prestamos', ['Deposito'])


    def backwards(self, orm):
        
        # Deleting model 'Financiador'
        db.delete_table('prestamos_financiador')

        # Deleting model 'Prestamo'
        db.delete_table('prestamos_prestamo')

        # Deleting model 'Cuota'
        db.delete_table('prestamos_cuota')

        # Deleting model 'Cuenta'
        db.delete_table('prestamos_cuenta')

        # Deleting model 'Deposito'
        db.delete_table('prestamos_deposito')


    models = {
        'contabilidad.moneda': {
            'Meta': {'object_name': 'Moneda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'}),
            'simbolo': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'prestamos.cuenta': {
            'Meta': {'object_name': 'Cuenta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minino': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contabilidad.Moneda']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'})
        },
        'prestamos.cuota': {
            'Meta': {'object_name': 'Cuota'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 6, 20, 16, 27, 55, 935059)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'}),
            'prestamo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prestamos.Prestamo']"})
        },
        'prestamos.deposito': {
            'Meta': {'object_name': 'Deposito'},
            'cuenta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prestamos.Cuenta']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 6, 20, 16, 27, 55, 936657)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'})
        },
        'prestamos.financiador': {
            'Meta': {'object_name': 'Financiador'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'})
        },
        'prestamos.prestamo': {
            'Meta': {'object_name': 'Prestamo'},
            'fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'financiador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prestamos.Financiador']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 6, 20, 16, 27, 55, 934235)'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contabilidad.Moneda']"}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'})
        }
    }

    complete_apps = ['prestamos']
