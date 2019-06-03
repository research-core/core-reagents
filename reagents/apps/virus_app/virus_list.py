from confapp import conf
from pyforms_web.organizers import no_columns, segment
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Virus

from .virus_form import VirusForm

class VirusAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Virus-app'.lower()
    MODEL = Virus
    
    TITLE = 'Virus'

    LIST_ROWS_PER_PAGE = 20

    LIST_DISPLAY = ('virus_name','virus_sequence','lab','supplier','contact',)
    LIST_HEADERS = ('Name','Sequence','Lab','Supplier','Contact',)

    LIST_FILTER = ('virus_type','supplier','lab',)
    SEARCH_FIELDS = [
        'virus_name__icontains',
        'virus_serotype__icontains',
        'virus_titter__icontains',
        'virus_dna_available__icontains',
        'virus_reference__icontains',
        'contact__icontains',
    ]

    EDITFORM_CLASS = VirusForm
   
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'bug red'
    ########################################################
    