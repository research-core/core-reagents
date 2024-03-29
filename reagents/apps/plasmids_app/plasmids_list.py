from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Plasmids

from .plasmids_form import PlasmidsForm

class PlasmidsAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Plasmids-app'.lower()
    MODEL = Plasmids
    
    TITLE = 'Plasmids'

    LIST_ROWS_PER_PAGE = 20

    LIST_DISPLAY = ('plasmid_name','vectortype','plasmid_reference','supplier','lab','contact',)
    LIST_FILTER = ('plasmid_name','vectortype','plasmid_system','plasmid_flippases','plasmid_attb','plasmid_marker','anti_resistance','growthstrain','supplier','lab',)
    SEARCH_FIELDS = [
        'plasmid_name__icontains',
        'plasmid_sc_enzymes__icontains',
        'plasmid_promoter__icontains',
        'plasmid_transgene__icontains',
        'plasmid_fluorchrome__icontains',
        'plasmid_seq_primers__icontains',
        'plasmid_sequence__icontains',
        'plasmid_temperature__icontains',
        'plasmid_reference__icontains',
        'contact__icontains',
    ]
    READ_ONLY = ('plasmid_id',)

    EDITFORM_CLASS = PlasmidsForm

    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'dna'
    ########################################################
    
    