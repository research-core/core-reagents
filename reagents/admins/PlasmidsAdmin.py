
from reagents.models import Plasmids
from django.forms import Textarea, CheckboxSelectMultiple
from django.forms.models import ModelMultipleChoiceField
from django.utils.translation import ugettext as _
from django.contrib import admin
from django.conf import settings
from django.db import models
#from common.admintools import export_xlsx, printable_html

class PlasmidsAdminAbstract(admin.ModelAdmin):

	list_display = ('plasmid_name','vectortype','contact',)
	list_filter = ('plasmid_name','vectortype','plasmid_system','plasmid_flippases','plasmid_attb','plasmid_marker','anti_resistance','growthstrain','supplier','lab',)
	search_fields = ['plasmid_id','plasmid_name','plasmid_mcs','plasmid_sc_enzymes','plasmid_promoter','plasmid_transgene','plasmid_fluorchrome','plasmid_seq_primers','plasmid_sequence','plasmid_temperature','plasmid_reference','contact',]
	readonly_fields = ('plasmid_id',)

	fieldsets = [
		('Plasmid',{
			'classes': ('suit-tab suit-tab-plasmid',),
			'fields': ['plasmid_name','vectortype','plasmid_mcs','plasmid_sc_enzymes','plasmid_backbone','plasmid_gateway','plasmid_vector']
		}),
		('Sequence information',{
			'classes': ('suit-tab suit-tab-plasmid',),
			'fields': ['plasmid_system','plasmid_flippases','plasmid_attb','plasmid_marker','plasmid_promoter','plasmid_transgene','plasmid_fluorchrome','plasmid_seq_primers','plasmid_sequence','plasmid_sequence2']
		}),
		('Growth in bacteria',{
			'classes': ('suit-tab suit-tab-plasmid',),
			'fields': ['anti_resistance','growthstrain','plasmid_temperature','plasmid_methylation']
		}),
		('Where to get it',{
			'classes': ('suit-tab suit-tab-plasmid',),
			'fields': ['plasmid_reference','supplier','lab','contact']
		}),
	]
	suit_form_tabs = [
		(u'plasmid', u'Plasmid')
	]


	radio_fields = {
		'plasmid_gateway': admin.VERTICAL,
		'plasmid_vector': admin.HORIZONTAL,
		'plasmid_system': admin.HORIZONTAL,
		'plasmid_flippases': admin.HORIZONTAL,
		'plasmid_attb': admin.HORIZONTAL,
		'plasmid_marker': admin.HORIZONTAL
	}

	#actions = [export_xlsx,]
				
	formfield_overrides = dict((
		(models.TextField,dict((( 'widget',Textarea(attrs=dict(rows=5, cols=120,style='width: 600px;') )),) )),
		(models.ManyToManyField,dict((('widget',CheckboxSelectMultiple),)))
	),)

	class Media:
		css = dict(all=['generic.css','fixadmin.css'])
		js = ('generic.js','models/plasmids.js')

	

	def get_actions(self, request):
		actions = super(PlasmidsAdminAbstract, self).get_actions(request)

		user = request.user
		#if not user.groups.filter(name=settings.HTML_EXPORTER_PROFILE_GROUP).exists(): del actions['printable_html']
		#if not user.groups.filter(name=settings.EXCEL_EXPORTER_PROFILE_GROUP).exists(): del actions['export_xlsx']
		return actions
			
	def construct_change_message(self, request, form, formsets, add=False):
		message = super(PlasmidsAdminAbstract, self).construct_change_message(request, form, formsets)
		change_message = []
		if form.changed_data:
			values = []
			for x in form.changed_data:
				field   = form.fields[x]
				initial = form.initial.get(x,None)				
				value 	= form.cleaned_data[x]
				if isinstance(field, ModelMultipleChoiceField): 
					value 	= [int(y.pk) for y in value]
					initial = [int(y) for y in initial] if initial!=None else []

				values.append( _(": %s -> %s" % (str(initial), str(value)) ) )
			change_message.append( '%s' % ','.join(values) )
			message += ' '.join(change_message)
		return message

				