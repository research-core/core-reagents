from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text




class AntibioticResistance(models.Model):
    
    antibioticresistance_id = models.AutoField("Antibiotic resistance id", primary_key=True)
    antibioticresistance_name = models.CharField("Antibiotic resistence name", max_length=100, unique=True)

    
    def __str__(self): return force_text(self.antibioticresistance_name)


    class Meta:
        verbose_name = "Antibiotic resistance"
        verbose_name_plural = "Antibiotic Resistances"
            