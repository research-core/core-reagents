##### auto:start:Enzyme #####
from abstractmodels.Enzyme import AbstractEnzyme

class Enzyme(AbstractEnzyme):
	pass
	##### auto:end:Enzyme #####
##### auto:start:Primer #####
from abstractmodels.Primer import AbstractPrimer

class Primer(AbstractPrimer):
	pass
	##### auto:end:Primer #####
##### auto:start:Antibody #####
from abstractmodels.Antibody import AbstractAntibody

class Antibody(AbstractAntibody):
	pass
	##### auto:end:Antibody #####
##### auto:start:Supplier #####
from abstractmodels.Supplier import AbstractSupplier

class Supplier(AbstractSupplier):
	pass
	##### auto:end:Supplier #####
##### auto:start:EnzymeType #####
from abstractmodels.EnzymeType import AbstractEnzymeType

class EnzymeType(AbstractEnzymeType):
	pass
	##### auto:end:EnzymeType #####
##### auto:start:Plasmids #####
from abstractmodels.Plasmids import AbstractPlasmids

class Plasmids(AbstractPlasmids):
	pass
	##### auto:end:Plasmids #####
##### auto:start:VectorType #####
from abstractmodels.VectorType import AbstractVectorType

class VectorType(AbstractVectorType):
	pass
	##### auto:end:VectorType #####
##### auto:start:Lab #####
from abstractmodels.Lab import AbstractLab

class Lab(AbstractLab):
	pass
	##### auto:end:Lab #####
##### auto:start:Reagent #####
from abstractmodels.Reagent import AbstractReagent

class Reagent(AbstractReagent):
	pass
	##### auto:end:Reagent #####
##### auto:start:Chemical #####
from abstractmodels.Chemical import AbstractChemical

class Chemical(AbstractChemical):
	pass
	##### auto:end:Chemical #####
##### auto:start:GrowthStrains #####
from abstractmodels.GrowthStrains import AbstractGrowthStrains

class GrowthStrains(AbstractGrowthStrains):
	pass
	##### auto:end:GrowthStrains #####
##### auto:start:AntibioticResistance #####
from abstractmodels.AntibioticResistance import AbstractAntibioticResistance

class AntibioticResistance(AbstractAntibioticResistance):
	pass
	##### auto:end:AntibioticResistance #####
