from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Reagent

class ReagentAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Reagent-app'.lower()
    MODEL = Reagent
    
    TITLE = 'Reagents'

    LIST_FILTER = ('supplier','lab',)
    SEARCH_FIELDS = [
        'reagent_name__icontains',
        'reagent_reagent__icontains',
        'reagent_purpose__icontains',
    ]
    READ_ONLY = ('reagent_id',)

    FIELDSETS = ['reagent_name','reagent_reagent','reagent_purpose','supplier','lab']

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left'
    ORQUESTRA_MENU_ORDER = 100
    ORQUESTRA_MENU_ICON  = 'database'
    ########################################################
    
    
    