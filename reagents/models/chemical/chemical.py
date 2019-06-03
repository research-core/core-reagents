from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text

from .chemical_queryset import ChemicalQuerySet


class Chemical(models.Model):
    chemical_id = models.AutoField("Chemical id", primary_key=True)
    chemical_name = models.CharField("Name", max_length=100)
    chemical_formula = models.CharField("Formula", max_length=50)
    chemical_purpose = models.TextField("Purpose", null=True,blank=True)
    chemical_reference = models.CharField("Reference", max_length=50)
    supplier = models.ForeignKey("Supplier", verbose_name="Supplier", on_delete=models.CASCADE)
    lab = models.ForeignKey("Lab", verbose_name="Lab", on_delete=models.CASCADE)
    contact = models.CharField("Person of contact", max_length=100, null=True,blank=True)

    objects = ChemicalQuerySet.as_manager()

    class Meta:
        verbose_name = "Chemical"
        verbose_name_plural = "Chemicals"
        unique_together = ('chemical_name', 'chemical_reference', 'supplier', 'lab',)