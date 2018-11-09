from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Plasmids

class PlasmidsAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Plasmids-app'.lower()
    MODEL = Plasmids
    
    TITLE = 'Plasmids'

    LIST_DISPLAY = ('plasmid_name','vectortype','plasmid_reference','supplier','lab','contact',)
    LIST_FILTER = ('plasmid_name','vectortype','plasmid_system','plasmid_flippases','plasmid_attb','plasmid_marker','anti_resistance','growthstrain','supplier','lab',)
    SEARCH_FIELDS = [
        'plasmid_id','plasmid_name__icontains',
        'plasmid_mcs','plasmid_sc_enzymes__icontains',
        'plasmid_promoter','plasmid_transgene__icontains',
        'plasmid_fluorchrome__icontains',
        'plasmid_seq_primers__icontains',
        'plasmid_sequence__icontains',
        'plasmid_temperature__icontains',
        'plasmid_reference__icontains',
        'contact__icontains',
    ]
    READ_ONLY = ('plasmid_id',)

    FIELDSETS = [{
        'Plasmid': ['plasmid_name','vectortype','plasmid_mcs','plasmid_sc_enzymes','plasmid_backbone','plasmid_gateway','plasmid_vector'],
        'Sequence information': ['plasmid_system','plasmid_flippases','plasmid_attb','plasmid_marker','plasmid_promoter','plasmid_transgene','plasmid_fluorchrome','plasmid_seq_primers','plasmid_sequence','plasmid_sequence2'],
        'Growth in bacteria': ['anti_resistance','growthstrain','plasmid_temperature','plasmid_methylation'],
        'Where to get it': ['plasmid_reference','supplier','lab','contact']
    }]
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'dna'
    ########################################################
    
    
    