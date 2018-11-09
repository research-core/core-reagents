from confapp import conf
from pyforms_web.organizers import no_columns, segment
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Enzyme

class EnzymeAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Enzyme-app'.lower()
    MODEL = Enzyme
    
    TITLE = 'Enzymes'

    LIST_ROWS_PER_PAGE = 20

    LIST_DISPLAY = ('enzyme_name','enzyme_reference','enzymetype','supplier','lab','contact',)
    LIST_FILTER = ('enzymetype','supplier','lab',)
    SEARCH_FIELDS = ['enzyme_reference__icontains','contact__icontains',]
    
    FIELDSETS = [
        ('enzyme_name', 'contact', 'lab'),
        'supplier',
        segment(
            ('enzyme_reference', 'enzymetype'),
            'enzyme_description',
        )
    ]

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'react'
    ########################################################
    
    
    