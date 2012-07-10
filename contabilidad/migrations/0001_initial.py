# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Moneda'
        db.create_table('contabilidad_moneda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=600)),
            ('simbolo', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('contabilidad', ['Moneda'])


    def backwards(self, orm):
        
        # Deleting model 'Moneda'
        db.delete_table('contabilidad_moneda')


    models = {
        'contabilidad.moneda': {
            'Meta': {'object_name': 'Moneda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'}),
            'simbolo': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        }
    }

    complete_apps = ['contabilidad']
