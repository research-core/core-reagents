from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text


class Enzyme(models.Model):
    enzyme_id = models.AutoField("Enzyme id", primary_key=True)
    enzyme_name = models.CharField("Name", max_length=50)
    enzyme_description = models.TextField("Description", null=True,blank=True)
    enzyme_reference = models.CharField("Reference", max_length=50)
    enzymetype = models.ForeignKey("EnzymeType", verbose_name="Type of enzyme", on_delete=models.CASCADE)
    supplier = models.ForeignKey("Supplier", verbose_name="Supplier", on_delete=models.CASCADE)
    lab = models.ForeignKey("Lab", verbose_name="Lab", on_delete=models.CASCADE)
    contact = models.CharField("Person of contact", max_length=100, null=True,blank=True)

    class Meta:
        verbose_name = "Enzyme"
        verbose_name_plural = "Enzymes"
        unique_together = ('enzyme_name', 'enzyme_reference', 'supplier', 'lab',)


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
        return getattr(self,'enzyme_name')!=None and \
            getattr(self,'enzyme_description')!=None and \
            getattr(self,'enzyme_reference')!=None and \
            getattr(self,'enzymetype')!=None and \
            getattr(self,'supplier')!=None and \
            getattr(self,'lab')!=None and \
            getattr(self,'contact')!=None
    is_complete.short_description="Complete"
    is_complete.boolean = True
            