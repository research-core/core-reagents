from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text


class Lab(models.Model):
    lab_id = models.AutoField("Lab id", primary_key=True)
    lab_name = models.CharField("Lab name", max_length=100)

    
    def __str__(self): return force_text(self.lab_name)


    class Meta:
        verbose_name = "Lab"
        verbose_name_plural = "Labs"

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
        return getattr(self,'lab_id')!=None and \
            getattr(self,'lab_name')!=None
    is_complete.short_description="Complete"
    is_complete.boolean = True
            