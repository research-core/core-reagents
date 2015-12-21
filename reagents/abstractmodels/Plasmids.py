from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




class AbstractPlasmid(models.Model):
	plasmid_id = models.AutoField("Plasmid id", primary_key=True)
	plasmid_name = models.CharField("Plasmid name", max_length=50)
	vectortype = models.ForeignKey("VectorType", verbose_name="Vector type")
	plasmid_mcs = models.BooleanField("Multiple Cloning Site (MCS)", default=False)

	class Meta: abstract = True

class AbstractWheretogetit(models.Model):
	plasmid_reference = models.CharField("Reference", max_length=50)
	supplier = models.ForeignKey("Supplier", verbose_name="Supplier")
	lab = models.ForeignKey("Lab", verbose_name="Lab")

	class Meta: abstract = True

class AbstractSequenceInformation(models.Model):
	plasmid_promoter = models.CharField("Promoter", max_length=50)
	plasmid_transgene = models.CharField("Transgene", max_length=50)
	plasmid_fluorchrome = models.CharField("Fluorchrome", max_length=50)
	plasmid_seq_primers = models.CharField("Sequencing primers", max_length=50)
	plasmid_sequence = models.FileField("Sequence 1", max_length=255, upload_to='uploads/abstractsequenceinformation')
	plasmid_sequence2 = models.FileField("Sequence 2", max_length=255, upload_to='uploads/abstractsequenceinformation', null=True,blank=True)

	class Meta: abstract = True

class AbstractGrowthinBacteria(models.Model):
	anti_resistance = models.ForeignKey("AntibioticResistance", verbose_name="Antibiotic resistance")
	growthstrain = models.ForeignKey("GrowthStrains", verbose_name="Growth strain", null=True,blank=True)
	plasmid_temperature = models.IntegerField("Temperature (C)", max_length=3)

	class Meta: abstract = True


class AbstractPlasmids(AbstractPlasmid,
	AbstractWheretogetit,
	AbstractSequenceInformation,
	AbstractGrowthinBacteria):
	
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
			getattr(self,'vectortype')!=None and \
			getattr(self,'plasmid_mcs')!=None and \
			getattr(self,'plasmid_promoter')!=None and \
			getattr(self,'plasmid_transgene')!=None and \
			getattr(self,'plasmid_fluorchrome')!=None and \
			getattr(self,'plasmid_seq_primers')!=None and \
			getattr(self,'plasmid_sequence')!=None and \
			getattr(self,'plasmid_sequence2')!=None and \
			getattr(self,'anti_resistance')!=None and \
			getattr(self,'growthstrain')!=None and \
			getattr(self,'plasmid_temperature')!=None and \
			getattr(self,'plasmid_reference')!=None and \
			getattr(self,'supplier')!=None and \
			getattr(self,'lab')!=None
	is_complete.short_description="Complete"
	is_complete.boolean = True
			