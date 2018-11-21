from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import VectorType

class VectorTypeAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-VectorType-app'.lower()
    MODEL = VectorType
    
    TITLE = 'Vector Types'

    LIST_DISPLAY = ['vectortype_name',]
    
    SEARCH_FIELDS = ['vectortype_name__icontains',]

    FIELDSETS = ['vectortype_name']
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 100
    ORQUESTRA_MENU_ICON  = 'database'
    ########################################################
    AUTHORIZED_GROUPS = ['superuser']