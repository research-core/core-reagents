from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text




class AbstractEnzymetype(models.Model):
	enzymetype_id = models.AutoField("Enzyme type id", primary_key=True)
	enzymetype_name = models.CharField("Enzyme type name", max_length=100, unique=True)

	class Meta: abstract = True


class AbstractEnzymeType(AbstractEnzymetype):
	
	def __unicode__(self): return force_text(self.enzymetype_name)


	class Meta:
		abstract = True
		verbose_name = "Enzyme type"
		verbose_name_plural = "Enzymes types"

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
		return getattr(self,'enzymetype_name')!=None
	is_complete.short_description="Complete"
	is_complete.boolean = True
			