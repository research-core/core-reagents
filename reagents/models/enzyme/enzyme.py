from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text


from .enzyme_queryset import EnzymeQuerySet

class Enzyme(models.Model):
    enzyme_id = models.AutoField("Enzyme id", primary_key=True)
    enzyme_name = models.CharField("Name", max_length=50)
    enzyme_description = models.TextField("Description", null=True,blank=True)
    enzyme_reference = models.CharField("Reference", max_length=50)
    enzymetype = models.ForeignKey("EnzymeType", verbose_name="Type of enzyme", on_delete=models.CASCADE)
    supplier = models.ForeignKey("Supplier", verbose_name="Supplier", on_delete=models.CASCADE)
    lab = models.ForeignKey("Lab", verbose_name="Lab", on_delete=models.CASCADE)
    contact = models.CharField("Person of contact", max_length=100, null=True,blank=True)

    objects = EnzymeQuerySet.as_manager()

    class Meta:
        verbose_name = "Enzyme"
        verbose_name_plural = "Enzymes"
        unique_together = ('enzyme_name', 'enzyme_reference', 'supplier', 'lab',)
