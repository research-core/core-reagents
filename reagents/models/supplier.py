from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text



class Supplier(models.Model):
    supplier_id = models.AutoField("Supplier id", primary_key=True)
    supplier_name = models.CharField("Supplier name", max_length=100, unique=True)

    def __str__(self): return force_text(self.supplier_name)


    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
