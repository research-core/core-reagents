from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Enzyme

class EnzymeAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Enzyme-app'.lower()
    MODEL = Enzyme
    
    TITLE = 'Enzymes'

    LIST_DISPLAY = ('enzyme_name','enzyme_reference','enzymetype','supplier','lab','contact',)
    LIST_FILTER = ('enzyme_id','enzymetype','supplier','lab',)
    SEARCH_FIELDS = ['enzyme_id','enzyme_reference__icontains','contact__icontains',]
    READ_ONLY = ('enzyme_id',)

    FIELDSETS = ['enzyme_name','enzyme_description','enzyme_reference','enzymetype','supplier','lab','contact']

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'database'
    ########################################################
    
    
    