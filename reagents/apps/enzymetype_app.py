from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import EnzymeType

class EnzymeTypeAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-EnzymeType-app'.lower()
    MODEL = EnzymeType
    
    TITLE = 'Enzymes Types'

    LIST_DISPLAY = ('enzymetype_name',)
    
    SEARCH_FIELDS = ['enzymetype_name__icontains',]

    FIELDSETS = ['enzymetype_name']
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 100
    ORQUESTRA_MENU_ICON  = 'database'
    ########################################################

    AUTHORIZED_GROUPS = ['superuser']