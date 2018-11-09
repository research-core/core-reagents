from confapp import conf
from pyforms_web.widgets.django import ModelFormWidget
from pyforms_web.organizers import no_columns, segment
from reagents.models import Plasmids


class PlasmidsForm(ModelFormWidget):
    

    MODEL = Plasmids
    
    TITLE = 'Plasmids editor'

    
    FIELDSETS = [{
        'a:Plasmid': ['plasmid_name','vectortype','plasmid_mcs','plasmid_sc_enzymes','plasmid_backbone','plasmid_gateway','plasmid_vector'],
        'b:Sequence information': ['plasmid_system','plasmid_flippases','plasmid_attb','plasmid_marker','plasmid_promoter','plasmid_transgene','plasmid_fluorchrome','plasmid_seq_primers','plasmid_sequence','plasmid_sequence2'],
        'c:Growth in bacteria': ['anti_resistance','growthstrain','plasmid_temperature','plasmid_methylation'],
        'd:Where to get it': ['plasmid_reference','supplier','lab','contact']
    }]

    FIELDSETS = [
        'h2:Plasmid',
        segment('plasmid_name',
            ('vectortype', 'plasmid_mcs'),
            'plasmid_sc_enzymes',
            ('plasmid_backbone', 'plasmid_gateway','plasmid_vector')
        ),
        'h2:Sequence information',
        segment(
            ('plasmid_system', 'plasmid_flippases', 'plasmid_attb', 'plasmid_marker'),
            ('plasmid_promoter', 'plasmid_transgene', 'plasmid_fluorchrome', 'plasmid_seq_primers'),
            ('plasmid_sequence', 'plasmid_sequence2')
        ),
        'h2:Growth in bacteria',
        segment(
            ('anti_resistance', 'growthstrain'),
            ('plasmid_temperature', 'plasmid_methylation')
        ),
        'h2:Where to get it',
        segment(
            ('plasmid_reference', 'supplier'),
            ('lab', 'contact')
        )
    ]
    
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ########################################################
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.plasmid_gateway.changed_event = self.__plasmid_gateway_changed_evt
        self.plasmid_mcs.changed_event = self.__plasmid_mcs_changed_evt
        self.vectortype.changed_event = self.__vectortype_changed_evt
        
        self.__plasmid_gateway_changed_evt()
        self.__plasmid_mcs_changed_evt()
        self.__vectortype_changed_evt()

    def __plasmid_gateway_changed_evt(self):
        if self.plasmid_gateway.value=='Y':
            self.plasmid_vector.show()
        else:
            self.plasmid_vector.hide()

    def __plasmid_mcs_changed_evt(self):
        if self.plasmid_mcs.value:
            self.plasmid_sc_enzymes.show()
        else:
            self.plasmid_sc_enzymes.hide()

    def __vectortype_changed_evt(self):
        if self.vectortype.value in [6,8]:
            self.plasmid_system.show()
            self.plasmid_flippases.show()
            self.plasmid_attb.show()
            self.plasmid_marker.show()
        else:
            self.plasmid_system.hide()
            self.plasmid_flippases.hide()
            self.plasmid_attb.hide()
            self.plasmid_marker.hide()