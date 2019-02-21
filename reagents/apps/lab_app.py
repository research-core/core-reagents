from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Lab

class LabAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-lab-app'
    MODEL = Lab
    
    TITLE = 'Labs'

    LIST_DISPLAY = ('lab_name','group')
    
    SEARCH_FIELDS = ['lab_name__icontains','group__group_name__icontains']


    FIELDSETS = ['lab_name', 'group']
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 100
    ORQUESTRA_MENU_ICON  = 'flask blue'
    ########################################################
    AUTHORIZED_GROUPS = ['superuser']