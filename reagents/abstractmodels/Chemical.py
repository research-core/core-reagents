from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




class AbstractChemical(models.Model):
	chemical_id = models.AutoField("Chemical id", primary_key=True)
	chemical_name = models.CharField("Name", max_length=50, unique=True)
	chemical_formula = models.CharField("Formula", max_length=50)
	chemical_purpose = models.TextField("Purpose", null=True,blank=True)
	chemical_reference = models.CharField("Reference", max_length=50)
	supplier = models.ForeignKey("Supplier", verbose_name="Supplier")
	lab = models.ForeignKey("Lab", verbose_name="Lab")

	class Meta: abstract = True


class AbstractChemical(AbstractChemical):
	
	def __unicode__(self): return str(self.chemical_name)


	class Meta:
		abstract = True
		verbose_name = "Chemical"
		verbose_name_plural = "Chemicals"

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
		return getattr(self,'chemical_name')!=None and \
			getattr(self,'chemical_formula')!=None and \
			getattr(self,'chemical_purpose')!=None and \
			getattr(self,'chemical_reference')!=None and \
			getattr(self,'supplier')!=None and \
			getattr(self,'lab')!=None
	is_complete.short_description="Complete"
	is_complete.boolean = True
			