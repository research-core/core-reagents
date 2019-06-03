from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text


class VectorType(models.Model):
    vectortype_id = models.AutoField("Vector type id", primary_key=True)
    vectortype_name = models.CharField("Vector type name", max_length=100, unique=True)

    def __str__(self): return force_text(self.vectortype_name)


    class Meta:
        verbose_name = "Vector type"
        verbose_name_plural = "Vector types"