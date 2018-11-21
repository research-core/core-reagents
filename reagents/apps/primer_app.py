from confapp import conf
from pyforms_web.organizers import no_columns, segment
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Primer

class PrimerAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Primer-app'.lower()
    MODEL = Primer
    
    TITLE = 'Primers'

    LIST_ROWS_PER_PAGE = 20

    LIST_DISPLAY = ('primer_name','primer_sequence','lab','supplier','contact',)
    LIST_FILTER = ('lab','supplier',)
    SEARCH_FIELDS = [
        'primer_name__icontains',
        'primer_sequence__icontains',
        'primer_purpose__icontains',
        'primer_melting_temp__icontains',
        'contact__icontains',
    ]
   

    FIELDSETS = [
        ('primer_name', 'contact', 'lab'),
        'supplier',
        segment(
            ('primer_sequence','primer_melting_temp'),
            'primer_purpose',
        )
    ]
   
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'dna'
    ########################################################
    
    
    