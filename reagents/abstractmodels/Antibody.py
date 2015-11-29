from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




class AbstractAntibody(models.Model):
	antibody_id = models.AutoField("Antibody id", primary_key=True)
	antibody_name = models.CharField("Name", max_length=50)
	antibody_target = models.CharField("Target", max_length=50)
	antibody_prim_sec = models.CharField("Primary/Secondary", max_length=50)
	antibody_conjuged2 = models.CharField("Conjugated to", max_length=50)
	antibody_reactivity = models.CharField("Reactivity", max_length=50)
	antibody_reference = models.CharField("Reference", max_length=50)
	supplier = models.ForeignKey("Supplier", verbose_name="Supplier")

	class Meta: abstract = True


class AbstractAntibody(AbstractAntibody):
	
	def __unicode__(self): return str(self.antibody_name)


	class Meta:
		abstract = True
		verbose_name = "Antibody"
		verbose_name_plural = "Antibodies"

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
		return getattr(self,'antibody_name')!=None and \
			getattr(self,'antibody_target')!=None and \
			getattr(self,'antibody_prim_sec')!=None and \
			getattr(self,'antibody_conjuged2')!=None and \
			getattr(self,'antibody_reactivity')!=None and \
			getattr(self,'antibody_reference')!=None and \
			getattr(self,'supplier')!=None
	is_complete.short_description="Complete"
	is_complete.boolean = True
			