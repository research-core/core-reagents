##### auto:start:Enzyme #####
from reagents.models import Enzyme
from reagents.admins.EnzymeAdmin import *

class EnzymeAdmin(EnzymeAdminAbstract):
	pass
	
	##### auto:end:Enzyme #####
##### auto:start:Primer #####
from reagents.models import Primer
from reagents.admins.PrimerAdmin import *

class PrimerAdmin(PrimerAdminAbstract):
	pass
	
	##### auto:end:Primer #####
##### auto:start:Antibody #####
from reagents.models import Antibody
from reagents.admins.AntibodyAdmin import *

class AntibodyAdmin(AntibodyAdminAbstract):
	pass
	
	##### auto:end:Antibody #####
##### auto:start:Supplier #####
from reagents.models import Supplier
from reagents.admins.SupplierAdmin import *

class SupplierAdmin(SupplierAdminAbstract):
	pass
	
	##### auto:end:Supplier #####
##### auto:start:EnzymeType #####
from reagents.models import EnzymeType
from reagents.admins.EnzymeTypeAdmin import *

class EnzymeTypeAdmin(EnzymeTypeAdminAbstract):
	pass
	
	##### auto:end:EnzymeType #####
##### auto:start:Plasmids #####
from reagents.models import Plasmids
from reagents.admins.PlasmidsAdmin import *

class PlasmidsAdmin(PlasmidsAdminAbstract):
	pass
	
	##### auto:end:Plasmids #####
admin.site.register(Enzyme, EnzymeAdmin)
admin.site.register(Primer, PrimerAdmin)
admin.site.register(Antibody, AntibodyAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(EnzymeType, EnzymeTypeAdmin)
admin.site.register(Plasmids, PlasmidsAdmin)
##### auto:start:VectorType #####
from reagents.models import VectorType
from reagents.admins.VectorTypeAdmin import *

class VectorTypeAdmin(VectorTypeAdminAbstract):
	pass
	
	##### auto:end:VectorType #####
admin.site.register(VectorType, VectorTypeAdmin)
##### auto:start:Lab #####
from reagents.models import Lab
from reagents.admins.LabAdmin import *

class LabAdmin(LabAdminAbstract):
	pass
	
	##### auto:end:Lab #####
admin.site.register(Lab, LabAdmin)
##### auto:start:Reagent #####
from models import Reagent
from admins.ReagentAdmin import *

class ReagentAdmin(ReagentAdminAbstract):
	pass
	
	##### auto:end:Reagent #####
admin.site.register(Reagent, ReagentAdmin)
##### auto:start:Chemical #####
from reagents.models import Chemical
from reagents.admins.ChemicalAdmin import *

class ChemicalAdmin(ChemicalAdminAbstract):
	pass
	
	##### auto:end:Chemical #####
##### auto:start:GrowthStrains #####
from reagents.models import GrowthStrains
from reagents.admins.GrowthStrainsAdmin import *

class GrowthStrainsAdmin(GrowthStrainsAdminAbstract):
	pass
	
	##### auto:end:GrowthStrains #####
##### auto:start:AntibioticResistance #####
from reagents.models import AntibioticResistance
from reagents.admins.AntibioticResistanceAdmin import *

class AntibioticResistanceAdmin(AntibioticResistanceAdminAbstract):
	pass
	
	##### auto:end:AntibioticResistance #####
admin.site.register(Chemical, ChemicalAdmin)
admin.site.register(GrowthStrains, GrowthStrainsAdmin)
admin.site.register(AntibioticResistance, AntibioticResistanceAdmin)
