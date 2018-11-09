from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import VectorType

class VectorTypeAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-VectorType-app'.lower()
    MODEL = VectorType
    
    TITLE = 'Vector Types'

    LIST_DISPLAY = ['vectortype_id','vectortype_name',]
    
    SEARCH_FIELDS = ['vectortype_id','vectortype_name__icontains',]
    READ_ONLY = ['vectortype_id',]

    FIELDSETS = ['vectortype_name']
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'database'
    ########################################################
    
    
    