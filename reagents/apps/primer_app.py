from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Primer

class PrimerAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Primer-app'.lower()
    MODEL = Primer
    
    TITLE = 'Primers'

    LIST_DISPLAY = ('primer_name','primer_sequence','lab','supplier','contact',)
    LIST_FILTER = ('primer_id','lab','supplier',)
    SEARCH_FIELDS = [
        'primer_id',
        'primer_name__icontains',
        'primer_sequence__icontains',
        'primer_purpose__icontains',
        'primer_melting_temp__icontains',
        'contact__icontains',
    ]
    READ_ONLY = ('primer_id',)

    FIELDSETS = ['primer_name','primer_sequence','primer_purpose','primer_melting_temp','lab','supplier','contact']
   
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'dna'
    ########################################################
    
    
    