from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from reagents.models import Supplier

class SupplierAdminApp(ModelAdminWidget):
    

    UID   = 'reagents-Supplier-app'.lower()
    MODEL = Supplier
    
    TITLE = 'Suppliers'

    LIST_DISPLAY = ('supplier_id','supplier_name',)
    
    SEARCH_FIELDS = ['supplier_id','supplier_name__icontains',]
    READ_ONLY = ('supplier_id',)

    FIELDSETS = ['supplier_name']
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>ReagentAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'truck'
    ########################################################
    
    
    