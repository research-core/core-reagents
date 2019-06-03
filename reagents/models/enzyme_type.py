from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text

class EnzymeType(models.Model):
    enzymetype_id = models.AutoField("Enzyme type id", primary_key=True)
    enzymetype_name = models.CharField("Enzyme type name", max_length=100, unique=True)

    def __str__(self): return force_text(self.enzymetype_name)


    class Meta:
        verbose_name = "Enzyme type"
        verbose_name_plural = "Enzymes types"
            