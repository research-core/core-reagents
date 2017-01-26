from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text




class AbstractPrimer(models.Model):
	primer_id = models.AutoField("Primer id", primary_key=True)
	primer_name = models.CharField("Name", max_length=50)
	primer_sequence = models.CharField("Sequence (5'-3')", max_length=100)
	primer_purpose = models.TextField("Purpose")
	primer_melting_temp = models.IntegerField("Melting Temperature (C)", max_length=3)
	lab = models.ForeignKey("Lab", verbose_name="Lab")
	supplier = models.ForeignKey("Supplier", verbose_name="Supplier")
	contact = models.CharField("Person of contact", max_length=100, null=True,blank=True)

	class Meta: abstract = True


class AbstractPrimer(AbstractPrimer):
	
	def __unicode__(self): return force_text(self.primer_name)

	def __str__(self): return str(self.__unicode__())


	class Meta:
		abstract = True
		verbose_name = "Primer"
		verbose_name_plural = "Primers"

	def ShowHideIf(self, checkingField, rules):
		values, listOfFields = rules
		values = values.split(';')
		if str(self.__dict__[checkingField]) in values:
			for field in listOfFields:
				if not self.__dict__[checkingField]!=None: return False
		return True
				
	def ShowHideIfManyToMany(self, checkingField, rules):
		values, listOfFields = rules
		values = values.split(';')
		
		selected = getattr(self,checkingField).all()
		active = False
		for v in selected:
			if v in values: 
				active=True
				break
		if active:
			for field in listOfFields:
				if self.__dict__[checkingField]==None: return False
		return True
				
	def is_complete(self):
		return getattr(self,'primer_name')!=None and \
			getattr(self,'primer_sequence')!=None and \
			getattr(self,'primer_purpose')!=None and \
			getattr(self,'primer_melting_temp')!=None and \
			getattr(self,'lab')!=None and \
			getattr(self,'supplier')!=None and \
			getattr(self,'contact')!=None
	is_complete.short_description="Complete"
	is_complete.boolean = True
			