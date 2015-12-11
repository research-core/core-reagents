from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




class AbstractEnzyme(models.Model):
	ensyme_id = models.AutoField("Enzyme id", primary_key=True)
	enzyme_name = models.CharField("Name", max_length=50)
	enzyme_description = models.TextField("Description", null=True,blank=True)
	enzyme_reference = models.CharField("Reference", max_length=50)
	enzymetype = models.ForeignKey("EnzymeType", verbose_name="Type of enzyme")
	supplier = models.ForeignKey("Supplier", verbose_name="Supplier")
	lab = models.ForeignKey("Lab", verbose_name="Lab")

	class Meta: abstract = True


class AbstractEnzyme(AbstractEnzyme):
	

	class Meta:
		abstract = True
		verbose_name = "Enzyme"
		verbose_name_plural = "Enzymes"

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
		return getattr(self,'enzyme_name')!=None and \
			getattr(self,'enzyme_description')!=None and \
			getattr(self,'enzyme_reference')!=None and \
			getattr(self,'enzymetype')!=None and \
			getattr(self,'supplier')!=None and \
			getattr(self,'lab')!=None
	is_complete.short_description="Complete"
	is_complete.boolean = True
			