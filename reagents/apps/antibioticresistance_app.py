from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import AntibioticResistance

class AntibioticResistanceAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-AntibioticResistance-app'.lower()
    MODEL = AntibioticResistance
    
    TITLE = 'Antibiotic Resistances'

    LIST_DISPLAY = ('antibioticresistance_name',)
    SEARCH_FIELDS = ['antibioticresistance_name__icontains',]
    
    FIELDSETS = ['antibioticresistance_name']

    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 98
    ORQUESTRA_MENU_ICON  = 'pills red'
    ########################################################
    
    AUTHORIZED_GROUPS = ['superuser']
    
    