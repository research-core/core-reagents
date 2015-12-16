##### auto:start:Enzyme #####
from models import Enzyme
from admins.EnzymeAdmin import *

class EnzymeAdmin(EnzymeAdminAbstract):
	pass
	
	##### auto:end:Enzyme #####
##### auto:start:Primer #####
from models import Primer
from admins.PrimerAdmin import *

class PrimerAdmin(PrimerAdminAbstract):
	pass
	
	##### auto:end:Primer #####
##### auto:start:Antibody #####
from models import Antibody
from admins.AntibodyAdmin import *

class AntibodyAdmin(AntibodyAdminAbstract):
	pass
	
	##### auto:end:Antibody #####
##### auto:start:Supplier #####
from models import Supplier
from admins.SupplierAdmin import *

class SupplierAdmin(SupplierAdminAbstract):
	pass
	
	##### auto:end:Supplier #####
##### auto:start:EnzymeType #####
from models import EnzymeType
from admins.EnzymeTypeAdmin import *

class EnzymeTypeAdmin(EnzymeTypeAdminAbstract):
	pass
	
	##### auto:end:EnzymeType #####
##### auto:start:Plasmids #####
from models import Plasmids
from admins.PlasmidsAdmin import *

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
from models import VectorType
from admins.VectorTypeAdmin import *

class VectorTypeAdmin(VectorTypeAdminAbstract):
	pass
	
	##### auto:end:VectorType #####
admin.site.register(VectorType, VectorTypeAdmin)
##### auto:start:Lab #####
from models import Lab
from admins.LabAdmin import *

class LabAdmin(LabAdminAbstract):
	pass
	
	##### auto:end:Lab #####
admin.site.register(Lab, LabAdmin)
##### auto:start:GrowthStrains #####
from models import GrowthStrains
from admins.GrowthStrainsAdmin import *

class GrowthStrainsAdmin(GrowthStrainsAdminAbstract):
	pass
	
	##### auto:end:GrowthStrains #####
##### auto:start:AntibioticResistance #####
from models import AntibioticResistance
from admins.AntibioticResistanceAdmin import *

class AntibioticResistanceAdmin(AntibioticResistanceAdminAbstract):
	pass
	
	##### auto:end:AntibioticResistance #####
admin.site.register(GrowthStrains, GrowthStrainsAdmin)
admin.site.register(AntibioticResistance, AntibioticResistanceAdmin)
##### auto:start:Chemical #####
from models import Chemical
from admins.ChemicalAdmin import *

class ChemicalAdmin(ChemicalAdminAbstract):
	pass
	
	##### auto:end:Chemical #####
admin.site.register(Chemical, ChemicalAdmin)