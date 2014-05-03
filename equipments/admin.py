from django.contrib import admin
from .models import Equipment
from actions import export_as_excel

class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('brand','family','model','specification')
	list_filter =  ('brand','model')
	search_fields = ( )
	list_editable = ('family','model',)
	raw_id_fields = ('brand',)
	actions = (export_as_excel,)

admin.site.register(Equipment,EquipmentAdmin)
