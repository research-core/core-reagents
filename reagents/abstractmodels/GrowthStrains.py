from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




class AbstractGrowthstrain(models.Model):
	growthstrain_id = models.AutoField("Growth strain id", primary_key=True)
	growthstrain_name = models.CharField("Growth strain name", max_length=100, unique=True)

	class Meta: abstract = True


class AbstractGrowthStrains(AbstractGrowthstrain):
	
	def __unicode__(self): return str(self.growthstrain_name)


	class Meta:
		abstract = True
		verbose_name = "Growth strain"
		verbose_name_plural = "Growth strains"

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
		return getattr(self,'growthstrain_name')!=None
	is_complete.short_description="Complete"
	is_complete.boolean = True
			