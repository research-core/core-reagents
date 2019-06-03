from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import VirusType

class VirusTypeAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-VirusType-app'.lower()
    MODEL = VirusType
    
    TITLE = 'Viruses Types'

    LIST_DISPLAY = ('virustype_name',)
    
    SEARCH_FIELDS = ['virustype_name__icontains',]

    FIELDSETS = ['virustype_name']
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 100
    ORQUESTRA_MENU_ICON  = 'database teal'
    ########################################################

    AUTHORIZED_GROUPS = ['superuser']