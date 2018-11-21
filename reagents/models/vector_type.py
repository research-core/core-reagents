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

    def ShowHideIf(self, checkingField, rules):
        values, listOfFields = rules
        values = values.split(';')
        if str(self.__dict__[checkingField]) in values:
            for field in listOfFields:
                if not self.__dict__[checkingField]!=None: return False
        return True
                
    def ShowHideIfManyToMany(self, checkingField, rules):
        values, listOfFields = rules
        values = values.split(';')
        
        selected = getattr(self,checkingField).all()
        active = False
        for v in selected:
            if v in values: 
                active=True
                break
        if active:
            for field in listOfFields:
                if self.__dict__[checkingField]==None: return False
        return True
                
    def is_complete(self):
        return getattr(self,'vectortype_name')!=None
    is_complete.short_description="Complete"
    is_complete.boolean = True
            