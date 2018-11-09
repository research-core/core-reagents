from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Antibody

class AntibodyAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Antibody-app'.lower()
    MODEL = Antibody
    
    TITLE = 'Antibodies'

    LIST_DISPLAY = ('antibody_name','antibody_target','antibody_reactivity','antibody_reference','supplier','lab','contact',)
    LIST_FILTER = ('antibody_id','supplier','lab',)
    SEARCH_FIELDS = [
        'antibody_id','antibody_name__icontains','antibody_target__icontains',
        'antibody_prim_sec__icontains','antibody_conjuged2__icontains',
        'antibody_reactivity__icontains','antibody_description__icontains',
        'antibody_applications__icontains','antibody_stock_concentration__icontains',
        'antibody_reference__icontains','contact__icontains',
    ]
    READ_ONLY = ('antibody_id',)

    FIELDSETS = ['antibody_name','antibody_target','antibody_prim_sec','antibody_conjuged2','antibody_reactivity','antibody_description','antibody_source','antibody_ig_class','antibody_applications','antibody_stock_concentration','antibody_working_concentration','antibody_reference','supplier','lab','contact','antibody_notes']
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'database'
    ########################################################
    
    
    