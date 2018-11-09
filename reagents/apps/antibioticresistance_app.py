from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import AntibioticResistance

class AntibioticResistanceAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-AntibioticResistance-app'.lower()
    MODEL = AntibioticResistance
    
    TITLE = 'Antibiotic Resistances'

    LIST_DISPLAY = ('antibioticresistance_id','antibioticresistance_name',)
    
    SEARCH_FIELDS = ['antibioticresistance_id','antibioticresistance_name__icontains',]
    READ_ONLY = ('antibioticresistance_id',)

    FIELDSETS = ['antibioticresistance_name']

    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'database'
    ########################################################
    
    
    