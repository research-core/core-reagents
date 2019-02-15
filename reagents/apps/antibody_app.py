from confapp import conf
from pyforms_web.organizers import no_columns, segment
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Antibody

class AntibodyAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Antibody-app'.lower()
    MODEL = Antibody
    
    TITLE = 'Antibodies'

    LIST_ROWS_PER_PAGE = 20

    LIST_DISPLAY = ('antibody_name','antibody_target','antibody_reactivity','antibody_reference','supplier','lab','contact',)
    LIST_FILTER = ('antibody_target', 'antibody_reactivity', 'supplier', 'lab',)
    SEARCH_FIELDS = [
        'antibody_name__icontains','antibody_target__icontains',
        'antibody_prim_sec__icontains','antibody_conjuged2__icontains',
        'antibody_reactivity__icontains','antibody_description__icontains',
        'antibody_applications__icontains','antibody_stock_concentration__icontains',
        'antibody_reference__icontains','contact__icontains',
    ]

    FIELDSETS = [
        ('antibody_name', 'contact', 'lab'),
        'supplier',
        segment(
            ('antibody_target', 'antibody_prim_sec', 'antibody_conjuged2'),
            ('antibody_reactivity', 'antibody_description', 'antibody_source'),
            ('antibody_ig_class', 'antibody_applications', 'antibody_stock_concentration'),
            ('antibody_working_concentration', 'antibody_reference', ' '),
        ),
        'antibody_notes'
    ]
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'circle outline green'
    ########################################################
    
    
    