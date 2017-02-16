##### auto:start:Enzyme #####
from abstractmodels.Enzyme import AbstractEnzyme

class Enzyme(AbstractEnzyme):
	pass
	##### auto:end:Enzyme #####
	class Meta:
		verbose_name = "Enzyme"
		verbose_name_plural = "Enzymes"
		unique_together = ('enzyme_name', 'enzyme_reference', 'supplier', 'lab',)

##### auto:start:Primer #####
from abstractmodels.Primer import AbstractPrimer

class Primer(AbstractPrimer):
	pass
	##### auto:end:Primer #####
	class Meta:
		verbose_name = "Primer"
		verbose_name_plural = "Primers"
		unique_together = ('primer_name', 'primer_sequence', 'supplier', 'lab',)

##### auto:start:Antibody #####
from abstractmodels.Antibody import AbstractAntibody

class Antibody(AbstractAntibody):
	pass
	##### auto:end:Antibody #####
	class Meta:
		verbose_name = "Antibody"
		verbose_name_plural = "Antibodies"
		unique_together = ('antibody_name', 'antibody_reference', 'supplier', 'lab',)

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
	class Meta:
		verbose_name = "Plasmid"
		verbose_name_plural = "Plasmids"
		unique_together = ('plasmid_name', 'plasmid_reference', 'supplier', 'lab',)

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
	class Meta:
		verbose_name = "Chemical"
		verbose_name_plural = "Chemicals"
		unique_together = ('chemical_name', 'chemical_reference', 'supplier', 'lab',)

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
