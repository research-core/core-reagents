from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




class AbstractAntibioticresistance(models.Model):
	antibioticresistance_id = models.AutoField("Antibiotic resistance id", primary_key=True)
	antibioticresistance_name = models.CharField("Antibiotic resistence name", max_length=100, unique=True)

	class Meta: abstract = True


class AbstractAntibioticResistance(AbstractAntibioticresistance):
	
	def __unicode__(self): return str(self.antibioticresistance_name)


	class Meta:
		abstract = True
		verbose_name = "Antibiotic resistance"
		verbose_name_plural = "Antibiotic Resistances"

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
		return getattr(self,'antibioticresistance_name')!=None
	is_complete.short_description="Complete"
	is_complete.boolean = True
			