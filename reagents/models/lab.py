from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text


class Lab(models.Model):
    lab_id = models.AutoField("Lab id", primary_key=True)
    lab_name = models.CharField("Lab name", max_length=100)

    group = models.ForeignKey('research.Group', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self): return force_text(self.lab_name)


    class Meta:
        verbose_name = "Lab"
        verbose_name_plural = "Labs"