from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text
from django.core.exceptions import ValidationError

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



class Plasmids(models.Model):
    plasmid_id = models.AutoField("Plasmid id", primary_key=True)
    plasmid_name = models.CharField("Plasmid name", max_length=50)
    vectortype = models.ForeignKey("VectorType", verbose_name="Vector type", on_delete=models.CASCADE)
    plasmid_mcs = models.BooleanField("Multiple Cloning Site (MCS)", default=False)
    plasmid_sc_enzymes = models.TextField("Single cutting enzymes", null=True,blank=True)
    plasmid_backbone = models.CharField("Backbone", max_length=100, null=True,blank=True)
    plasmid_gateway = models.CharField("""Gateway""", choices=BOOLEAN, max_length=10, null=True,blank=True)
    plasmid_vector = models.CharField("""Vector""", choices=PLASMIDS_VECTOR, max_length=10, null=True,blank=True)

    plasmid_reference = models.CharField("Reference", max_length=50)
    supplier = models.ForeignKey("Supplier", verbose_name="Supplier", on_delete=models.CASCADE)
    lab = models.ForeignKey("Lab", verbose_name="Lab", on_delete=models.CASCADE)
    contact = models.CharField("Person of contact", max_length=100, null=True,blank=True)

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

    
    anti_resistance = models.ForeignKey("AntibioticResistance", verbose_name="Antibiotic resistance", on_delete=models.CASCADE)
    growthstrain = models.ForeignKey("GrowthStrains", verbose_name="Growth strain", null=True,blank=True, on_delete=models.CASCADE)
    plasmid_temperature = models.IntegerField("Temperature (C)")
    plasmid_methylation = models.CharField("Methylation", max_length=100, null=True,blank=True)


    

    

    class Meta:
        verbose_name = "Plasmid"
        verbose_name_plural = "Plasmids"
        unique_together = ('plasmid_name', 'plasmid_reference', 'supplier', 'lab',)

    def __str__(self): return force_text(self.plasmid_name)


    """
    def clean(self):

        if self.plasmid_gateway=='Y':
            
        else:
            self.plasmid_vector.hide()

    
        if self.plasmid_mcs=='on':
            self.plasmid_sc_enzymes.show()
        else:
            self.plasmid_sc_enzymes.hide()

    
        if self.vectortype in [6,8]:
            self.plasmid_system.show()
            self.plasmid_flippases.show()
            self.plasmid_attb.show()
            self.plasmid_marker.show()
        else:
            self.plasmid_system.hide()
            self.plasmid_flippases.hide()
            self.plasmid_attb.hide()
            self.plasmid_marker.hide()
    """