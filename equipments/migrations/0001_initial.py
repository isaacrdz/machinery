# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Equipment'
        db.create_table(u'equipments_equipment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brands.Brand'])),
            ('family', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['families.Family'])),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('specification', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'equipments', ['Equipment'])


    def backwards(self, orm):
        # Deleting model 'Equipment'
        db.delete_table(u'equipments_equipment')


    models = {
        u'brands.brand': {
            'Meta': {'object_name': 'Brand'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'equipments.equipment': {
            'Meta': {'object_name': 'Equipment'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brands.Brand']"}),
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['families.Family']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'specification': ('django.db.models.fields.TextField', [], {})
        },
        u'families.family': {
            'Meta': {'object_name': 'Family'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['equipments']