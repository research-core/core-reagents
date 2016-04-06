from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


BOOLEAN = (
	('N',"""No"""),
	('Y',"""Yes"""),
)

PLASMIDS_SYSTEM = (
	('G',"""GAL4/UAS"""),
	('Q',"""Q"""),
	('L',"""LexA"""),
)

PLASMIDS_MARKER = (
	('W',"""White gene"""),
	('M',"""Mini white gene"""),
)

PLASMIDS_VECTOR = (
	('DO',"""Donor vector"""),
	('DE',"""Destination"""),
)



class AbstractPlasmid(models.Model):
	plasmid_id = models.AutoField("Plasmid id", primary_key=True)
	plasmid_name = models.CharField("Plasmid name", max_length=50)
	vectortype = models.ForeignKey("VectorType", verbose_name="Vector type")
	plasmid_mcs = models.BooleanField("Multiple Cloning Site (MCS)", default=False)
	plasmid_sc_enzymes = models.TextField("Single cutting enzymes", null=True,blank=True)
	plasmid_backbone = models.CharField("Backbone", max_length=100, null=True,blank=True)
	plasmid_gateway = models.CharField("""Gateway""", choices=BOOLEAN, max_length=10, null=True,blank=True)
	plasmid_vector = models.CharField("""Vector""", choices=PLASMIDS_VECTOR, max_length=10, null=True,blank=True)

	class Meta: abstract = True

class AbstractWheretogetit(models.Model):
	plasmid_reference = models.CharField("Reference", max_length=50)
	supplier = models.ForeignKey("Supplier", verbose_name="Supplier")
	lab = models.ForeignKey("Lab", verbose_name="Lab")
	contact = models.CharField("Person of contact", max_length=100, null=True,blank=True)

	class Meta: abstract = True

class AbstractSequenceInformation(models.Model):
	plasmid_system = models.CharField("""System""", choices=PLASMIDS_SYSTEM, max_length=10, null=True,blank=True)
	plasmid_flippases = models.CharField("""Flippases""", choices=BOOLEAN, max_length=10, null=True,blank=True)
	plasmid_attb = models.CharField("""attB""", choices=BOOLEAN, max_length=10, null=True,blank=True)
	plasmid_marker = models.CharField("""Marker""", choices=PLASMIDS_MARKER, max_length=10, null=True,blank=True)
	plasmid_promoter = models.CharField("Promoter", max_length=50)
	plasmid_transgene = models.CharField("Transgene", max_length=50)
	plasmid_fluorchrome = models.CharField("Fluorochrome", max_length=50, null=True,blank=True)
	plasmid_seq_primers = models.CharField("Sequencing primers", max_length=50)
	plasmid_sequence = models.FileField("Map", max_length=255, upload_to='uploads/abstractsequenceinformation')
	plasmid_sequence2 = models.FileField("Sequence", max_length=255, upload_to='uploads/abstractsequenceinformation', null=True,blank=True)

	class Meta: abstract = True

class AbstractGrowthinBacteria(models.Model):
	anti_resistance = models.ForeignKey("AntibioticResistance", verbose_name="Antibiotic resistance")
	growthstrain = models.ForeignKey("GrowthStrains", verbose_name="Growth strain", null=True,blank=True)
	plasmid_temperature = models.IntegerField("Temperature (C)", max_length=3)
	plasmid_methylation = models.CharField("Methylation", max_length=100, null=True,blank=True)

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
		return self.ShowHideIf('plasmid_gateway','TRUE;', ['plasmid_vector']) and \
			self.ShowHideIf('vectortype','7;8', ['plasmid_system', 'plasmid_flippases', 'plasmid_attb', 'plasmid_marker']) and \
			self.ShowHideIf('plasmid_mcs','on;', ['plasmid_sc_enzymes']) and \
			getattr(self,'plasmid_name')!=None and \
			getattr(self,'vectortype')!=None and \
			getattr(self,'plasmid_mcs')!=None and \
			getattr(self,'plasmid_sc_enzymes')!=None and \
			getattr(self,'plasmid_system')!=None and \
			getattr(self,'plasmid_flippases')!=None and \
			getattr(self,'plasmid_attb')!=None and \
			getattr(self,'plasmid_marker')!=None and \
			getattr(self,'plasmid_promoter')!=None and \
			getattr(self,'plasmid_transgene')!=None and \
			getattr(self,'plasmid_fluorchrome')!=None and \
			getattr(self,'plasmid_seq_primers')!=None and \
			getattr(self,'plasmid_sequence')!=None and \
			getattr(self,'plasmid_sequence2')!=None and \
			getattr(self,'anti_resistance')!=None and \
			getattr(self,'growthstrain')!=None and \
			getattr(self,'plasmid_temperature')!=None and \
			getattr(self,'plasmid_methylation')!=None and \
			getattr(self,'plasmid_reference')!=None and \
			getattr(self,'supplier')!=None and \
			getattr(self,'lab')!=None and \
			getattr(self,'contact')!=None and \
			getattr(self,'plasmid_backbone')!=None and \
			getattr(self,'plasmid_gateway')!=None and \
			getattr(self,'plasmid_vector')!=None
	is_complete.short_description="Complete"
	is_complete.boolean = True
			