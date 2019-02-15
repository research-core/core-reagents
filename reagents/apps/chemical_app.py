from confapp import conf
from pyforms_web.organizers import no_columns, segment
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Chemical

class ChemicalAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Chemical-app'.lower()
    MODEL = Chemical
    
    TITLE = 'Chemicals'

    LIST_ROWS_PER_PAGE = 20

    LIST_DISPLAY = ('chemical_name','chemical_formula','chemical_reference','supplier','lab','contact',)
    LIST_FILTER = ('supplier','lab',)
    SEARCH_FIELDS = [
        'chemical_name__icontains',
        'chemical_formula__icontains','chemical_purpose__icontains',
        'chemical_reference__icontains','contact__icontains',
    ]

    FIELDSETS = [
        ('chemical_name', 'contact', 'lab'),
        'supplier',
        segment(
            'chemical_reference', 'chemical_formula',
            'chemical_purpose',
        )
    ]
   
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'flask orange'
    ########################################################
    
    
    