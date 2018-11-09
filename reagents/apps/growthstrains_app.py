from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import GrowthStrains

class GrowthStrainsAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-GrowthStrains-app'.lower()
    MODEL = GrowthStrains
    
    TITLE = 'Growth Strains'

    LIST_DISPLAY = ('growthstrain_id','growthstrain_name',)
    
    SEARCH_FIELDS = ['growthstrain_id','growthstrain_name__icontains',]
    READ_ONLY = ('growthstrain_id',)

    FIELDSETS = ['growthstrain_name']
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'database'
    ########################################################
    
    
    