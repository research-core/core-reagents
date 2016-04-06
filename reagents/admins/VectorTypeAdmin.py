
from reagents.models import VectorType
from django.forms import Textarea, CheckboxSelectMultiple
from django.forms.models import ModelMultipleChoiceField
from django.utils.translation import ugettext as _
from django.contrib import admin
from django.conf import settings
from django.db import models
#from common.admintools import export_xlsx, printable_html

class VectorTypeAdminAbstract(admin.ModelAdmin):

	list_display = ('vectortype_id','vectortype_name',)
	
	search_fields = ['vectortype_id','vectortype_name',]
	readonly_fields = ('vectortype_id',)

	fieldsets = [
		('',{
			'classes': ('suit-tab suit-tab-enzymetype',),
			'fields': ['vectortype_name']
		}),
	]
	suit_form_tabs = [
		(u'enzymetype', u'Enzyme type')
	]


	

	#actions = [export_xlsx,]
				
	formfield_overrides = dict((
		(models.TextField,dict((( 'widget',Textarea(attrs=dict(rows=5, cols=120,style='width: 600px;') )),) )),
		(models.ManyToManyField,dict((('widget',CheckboxSelectMultiple),)))
	),)

	class Media:
		css = dict(all=['generic.css','fixadmin.css'])
		js = ('generic.js','models/vectortype.js')

	

	def get_actions(self, request):
		actions = super(VectorTypeAdminAbstract, self).get_actions(request)

		user = request.user
		#if not user.groups.filter(name=settings.HTML_EXPORTER_PROFILE_GROUP).exists(): del actions['printable_html']
		#if not user.groups.filter(name=settings.EXCEL_EXPORTER_PROFILE_GROUP).exists(): del actions['export_xlsx']
		return actions
			
	def construct_change_message(self, request, form, formsets, add=False):
		message = super(VectorTypeAdminAbstract, self).construct_change_message(request, form, formsets)
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

				