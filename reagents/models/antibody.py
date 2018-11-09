from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import force_text




class Antibody(models.Model):
    antibody_id = models.AutoField("Antibody id", primary_key=True)
    antibody_name = models.CharField("Name", max_length=100, help_text="""(p.e. "anti-Something")""")
    antibody_target = models.CharField("Target", max_length=50, help_text="""(p.e. "Something")""")
    antibody_prim_sec = models.CharField("Primary/Secondary/Tracer", max_length=50)
    antibody_conjuged2 = models.CharField("Conjugated to", max_length=50, help_text="""(p.e. "Alexa Fluor 488"; "Unconjugated")""")
    antibody_reactivity = models.CharField("Reactivity", max_length=100, help_text="""(species the Ab is know to react to)""")
    antibody_description = models.CharField("Description", max_length=50, null=True,blank=True)
    antibody_source = models.CharField("Source", max_length=100, help_text="""(specie the Ab was raised in; p.e. "Mouse")""", null=True,blank=True)
    antibody_ig_class = models.CharField("Ig class", max_length=50, help_text="""(Polyclonal vs. Monoclonal; add IgG class when available)""", null=True,blank=True)
    antibody_applications = models.CharField("Applications", max_length=50, help_text="""(p.e. "WB"; "ICC/IF")""", null=True,blank=True)
    antibody_stock_concentration = models.CharField("Stock Concentration", max_length=50, null=True,blank=True)
    antibody_working_concentration = models.CharField("Working concentration", max_length=50, null=True,blank=True)
    antibody_reference = models.CharField("Reference", max_length=50)
    supplier = models.ForeignKey("Supplier", verbose_name="Supplier", on_delete=models.CASCADE)
    lab = models.ForeignKey("Lab", verbose_name="Lab", default=True, on_delete=models.CASCADE)
    contact = models.CharField("Person of contact", max_length=100, null=True,blank=True)
    antibody_notes = models.TextField("Notes", null=True,blank=True)

    class Meta:
        verbose_name = "Antibody"
        verbose_name_plural = "Antibodies"
        unique_together = ('antibody_name', 'antibody_reference', 'supplier', 'lab',)

    def __str__(self): return force_text(self.antibody_name)


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
        return getattr(self,'antibody_name')!=None and \
            getattr(self,'antibody_target')!=None and \
            getattr(self,'antibody_prim_sec')!=None and \
            getattr(self,'antibody_conjuged2')!=None and \
            getattr(self,'antibody_reactivity')!=None and \
            getattr(self,'antibody_description')!=None and \
            getattr(self,'antibody_source')!=None and \
            getattr(self,'antibody_ig_class')!=None and \
            getattr(self,'antibody_applications')!=None and \
            getattr(self,'antibody_stock_concentration')!=None and \
            getattr(self,'antibody_working_concentration')!=None and \
            getattr(self,'antibody_reference')!=None and \
            getattr(self,'supplier')!=None and \
            getattr(self,'lab')!=None and \
            getattr(self,'contact')!=None and \
            getattr(self,'antibody_notes')!=None
    is_complete.short_description="Complete"
    is_complete.boolean = True
            