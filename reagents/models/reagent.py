from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




class Reagent(models.Model):
    reagent_id = models.AutoField("Reagent id", primary_key=True)
    reagent_name = models.CharField("Name", max_length=50, unique=True)
    reagent_reagent = models.CharField("Reagent", max_length=50)
    reagent_purpose = models.TextField("Purpose", null=True,blank=True)
    supplier = models.ForeignKey("Supplier", verbose_name="Supplier", on_delete=models.CASCADE)
    lab = models.ForeignKey("Lab", verbose_name="Lab", on_delete=models.CASCADE)

    
    def __str__(self): return str(self.reagent_name)


    class Meta:
        verbose_name = "Reagent"
        verbose_name_plural = "Reagents"

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
        return getattr(self,'reagent_name')!=None and \
            getattr(self,'reagent_reagent')!=None and \
            getattr(self,'reagent_purpose')!=None and \
            getattr(self,'supplier')!=None and \
            getattr(self,'lab')!=None
    is_complete.short_description="Complete"
    is_complete.boolean = True
            