from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text

from .virus_queryset import VirusQuerySet

BOOLEAN = (
    ('N',"""No"""),
    ('Y',"""Yes"""),
)

class Virus(models.Model):
    virus_id = models.AutoField("Virus id", primary_key=True)
    virus_name = models.CharField("Name", max_length=50)
    virus_type = models.ForeignKey("VirusType", verbose_name="Virus type", on_delete=models.CASCADE)
    virus_serotype = models.CharField("Serotype", max_length=50, null=True, blank=True)  
    virus_titter = models.CharField("Titter", max_length=50)
    virus_dna_available = models.CharField("DNA available", choices=BOOLEAN, max_length=10, null=True, blank=True)

    virus_reference = models.CharField("Reference", max_length=50)
    supplier = models.ForeignKey("Supplier", verbose_name="Supplier", on_delete=models.CASCADE)
    lab = models.ForeignKey("Lab", verbose_name="Lab", on_delete=models.CASCADE)
    contact = models.CharField("Person of contact", max_length=100, null=True,blank=True)

    objects = VirusQuerySet.as_manager()


    class Meta:
        verbose_name = "Virus"
        verbose_name_plural = "Viruses"
        unique_together = ('virus_name', 'virus_reference', 'supplier', 'lab',)