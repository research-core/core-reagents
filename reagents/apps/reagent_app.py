from confapp import conf
from pyforms_web.organizers import no_columns, segment
from pyforms.basewidget import BaseWidget


class ReagentAdminApp(BaseWidget):

    UID   = 'reagents-db'
    TITLE = 'Reagents'

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left'
    ORQUESTRA_MENU_ORDER = 100
    ORQUESTRA_MENU_ICON  = 'database yellow'
    ########################################################

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.formset = [
            """h3:The reagents database contains information about the diferent reagents available on the Labs, and that can be shared amoung the CR community.""",
            """You will find here: <br/><ul><li>Antibodies</li><li>Chemicals</li><li>Enzymes</li><li>Plasmids</li><li>Primers</li></ul><li>Virus</li></ul>"""
        ]
    
    
    