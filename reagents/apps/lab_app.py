from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Lab

class LabAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Lab-app'.lower()
    MODEL = Lab
    
    TITLE = 'Labs'

    LIST_DISPLAY = ('lab_name',)
    
    SEARCH_FIELDS = ['lab_name__icontains',]
    READ_ONLY = ('lab_id',)

    FIELDSETS = ['lab_id','lab_name']
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'flask'
    ########################################################
    
    
    