from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text


class GrowthStrains(models.Model):
    growthstrain_id = models.AutoField("Growth strain id", primary_key=True)
    growthstrain_name = models.CharField("Growth strain name", max_length=100, unique=True)

    def __str__(self): return force_text(self.growthstrain_name)


    class Meta:
        verbose_name = "Growth strain"
        verbose_name_plural = "Growth strains"
            