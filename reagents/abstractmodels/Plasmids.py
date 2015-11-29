from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




class AbstractGroup2(models.Model):
	plasmid_transgene = models.CharField("Transgene", max_length=50)
	plasmid_fluorchrome = models.CharField("Fluorchrome", max_length=50)
	plasmid_anti_resistance = models.CharField("Antibiotic resistance", max_length=50)

	class Meta: abstract = True

class AbstractGroup3(models.Model):
	plasmid_growthstrains = models.CharField("Growth strains", max_length=50)
	plasmid_system = models.CharField("System", max_length=50)
	plasmid_reference = models.CharField("Reference", max_length=50)
	plasmid_seq_primers = models.CharField("Sequencing primers", max_length=50)
	plasmid_sequence = models.CharField("Sequence", max_length=50)
	vectortype = models.ForeignKey("VectorType", verbose_name="Vector type")
	supplier = models.ForeignKey("Supplier", verbose_name="Supplier")
	lab = models.ForeignKey("Lab", verbose_name="Lab")

	class Meta: abstract = True

class AbstractGroup1(models.Model):
	plasmid_id = models.AutoField("Plasmid id", primary_key=True)
	plasmid_name = models.CharField("Plasmid name", max_length=50)
	plasmid_promoter = models.CharField("Promoter", max_length=50)

	class Meta: abstract = True


class AbstractPlasmids(AbstractGroup2,
	AbstractGroup3,
	AbstractGroup1):
	
	def __unicode__(self): return str(self.plasmid_name)


	class Meta:
		abstract = True
		verbose_name = "Plasmid"
		verbose_name_plural = "Plasmids"

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
		return getattr(self,'plasmid_name')!=None and \
			getattr(self,'plasmid_promoter')!=None and \
			getattr(self,'plasmid_transgene')!=None and \
			getattr(self,'plasmid_fluorchrome')!=None and \
			getattr(self,'plasmid_anti_resistance')!=None and \
			getattr(self,'plasmid_growthstrains')!=None and \
			getattr(self,'plasmid_system')!=None and \
			getattr(self,'plasmid_reference')!=None and \
			getattr(self,'plasmid_seq_primers')!=None and \
			getattr(self,'plasmid_sequence')!=None and \
			getattr(self,'vectortype')!=None and \
			getattr(self,'supplier')!=None and \
			getattr(self,'lab')!=None
	is_complete.short_description="Complete"
	is_complete.boolean = True
			