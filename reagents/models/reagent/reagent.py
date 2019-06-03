from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


from .reagent_queryset import ReagentQuerySet

class Reagent(models.Model):
    reagent_id = models.AutoField("Reagent id", primary_key=True)
    reagent_name = models.CharField("Name", max_length=50, unique=True)
    reagent_reagent = models.CharField("Reagent", max_length=50)
    reagent_purpose = models.TextField("Purpose", null=True,blank=True)
    supplier = models.ForeignKey("Supplier", verbose_name="Supplier", on_delete=models.CASCADE)
    lab = models.ForeignKey("Lab", verbose_name="Lab", on_delete=models.CASCADE)

    objects = ReagentQuerySet.as_manager()
    
    def __str__(self): return str(self.reagent_name)


    class Meta:
        verbose_name = "Reagent"
        verbose_name_plural = "Reagents"