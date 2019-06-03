from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text

from .primer_queryset import PrimerQuerySet

class Primer(models.Model):
    primer_id = models.AutoField("Primer id", primary_key=True)
    primer_name = models.CharField("Name", max_length=50)
    primer_sequence = models.CharField("Sequence (5'-3')", max_length=100)
    primer_purpose = models.TextField("Purpose")
    primer_melting_temp = models.IntegerField("Melting Temperature (C)")
    lab = models.ForeignKey("Lab", verbose_name="Lab", on_delete=models.CASCADE)
    supplier = models.ForeignKey("Supplier", verbose_name="Supplier", on_delete=models.CASCADE)
    contact = models.CharField("Person of contact", max_length=100, null=True,blank=True)

    objects = PrimerQuerySet.as_manager()

    class Meta:
        verbose_name = "Primer"
        verbose_name_plural = "Primers"
        unique_together = ('primer_name', 'primer_sequence', 'supplier', 'lab',)
            