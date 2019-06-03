from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text

class VirusType(models.Model):
    virustype_id = models.AutoField("Virus type id", primary_key=True)
    virustype_name = models.CharField("Virus type name", max_length=100, unique=True)

    def __str__(self): return force_text(self.virustype_name)


    class Meta:
        verbose_name = "Virus type"
        verbose_name_plural = "Viruses types"
            