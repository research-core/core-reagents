from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Chemical

class ChemicalAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Chemical-app'.lower()
    MODEL = Chemical
    
    TITLE = 'Chemicals'

    LIST_DISPLAY = ('chemical_name','chemical_formula','chemical_reference','supplier','lab','contact',)
    LIST_FILTER = ('supplier','lab',)
    SEARCH_FIELDS = [
        'chemical_name__icontains',
        'chemical_formula__icontains','chemical_purpose__icontains',
        'chemical_reference__icontains','contact__icontains',
    ]
    READ_ONLY = ('chemical_id',)

    FIELDSETS = ['chemical_name','chemical_formula','chemical_purpose','chemical_reference','supplier','lab','contact']
   
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'flask'
    ########################################################
    
    
    