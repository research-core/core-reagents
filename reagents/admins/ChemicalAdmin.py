
from reagents.models import Chemical
from django.forms import Textarea, CheckboxSelectMultiple
from django.forms.models import ModelMultipleChoiceField
from django.utils.translation import ugettext as _
from django.contrib import admin
from django.conf import settings
from django.db import models
#from common.admintools import export_xlsx, printable_html

class ChemicalAdminAbstract(admin.ModelAdmin):

	list_display = ('chemical_name','chemical_formula',)
	list_filter = ('supplier','lab',)
	search_fields = ['chemical_name','chemical_formula','chemical_purpose','chemical_reference',]
	readonly_fields = ('chemical_id',)

	fieldsets = [
		('',{
			'classes': ('suit-tab suit-tab-chemical',),
			'fields': ['chemical_name','chemical_formula','chemical_purpose','chemical_reference','supplier','lab']
		}),
	]
	suit_form_tabs = [
		(u'chemical', u'Chemical')
	]


	

	#actions = [export_xlsx,]
				
	formfield_overrides = dict((
		(models.TextField,dict((( 'widget',Textarea(attrs=dict(rows=5, cols=120,style='width: 600px;') )),) )),
		(models.ManyToManyField,dict((('widget',CheckboxSelectMultiple),)))
	),)

	class Media:
		css = dict(all=['generic.css','fixadmin.css'])
		js = ('generic.js','models/chemical.js')

	

	def get_actions(self, request):
		actions = super(ChemicalAdminAbstract, self).get_actions(request)

		user = request.user
		#if not user.groups.filter(name=settings.HTML_EXPORTER_PROFILE_GROUP).exists(): del actions['printable_html']
		#if not user.groups.filter(name=settings.EXCEL_EXPORTER_PROFILE_GROUP).exists(): del actions['export_xlsx']
		return actions
			
	def construct_change_message(self, request, form, formsets):
		message = super(ChemicalAdminAbstract, self).construct_change_message(request, form, formsets)
		change_message = []
		if form.changed_data:
			values = []
			for x in form.changed_data:
				field   = form.fields[x]
				initial = form.initial[x]
				value 	= form.cleaned_data[x]
				if isinstance(field, ModelMultipleChoiceField): 
					value 	= [int(y.pk) for y in value]
					initial = [int(y) for y in initial]

				values.append( _("<b>%s</b>: <span style='color:#4682B4' >%s</span> -> <span style='color:#00A600' >%s</span>" % (x, str(initial), str(value)) ) )
			change_message.append( '<ul><li>%s</li></ul>' % '</li><li>'.join(values) )
			message += ' '.join(change_message)
		return message

				