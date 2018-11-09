from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text




class Chemical(models.Model):
    chemical_id = models.AutoField("Chemical id", primary_key=True)
    chemical_name = models.CharField("Name", max_length=100)
    chemical_formula = models.CharField("Formula", max_length=50)
    chemical_purpose = models.TextField("Purpose", null=True,blank=True)
    chemical_reference = models.CharField("Reference", max_length=50)
    supplier = models.ForeignKey("Supplier", verbose_name="Supplier", on_delete=models.CASCADE)
    lab = models.ForeignKey("Lab", verbose_name="Lab", on_delete=models.CASCADE)
    contact = models.CharField("Person of contact", max_length=100, null=True,blank=True)

    class Meta:
        verbose_name = "Chemical"
        verbose_name_plural = "Chemicals"
        unique_together = ('chemical_name', 'chemical_reference', 'supplier', 'lab',)


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
        return getattr(self,'chemical_name')!=None and \
            getattr(self,'chemical_formula')!=None and \
            getattr(self,'chemical_purpose')!=None and \
            getattr(self,'chemical_reference')!=None and \
            getattr(self,'supplier')!=None and \
            getattr(self,'lab')!=None and \
            getattr(self,'contact')!=None
    is_complete.short_description="Complete"
    is_complete.boolean = True
            