from confapp import conf
from pyforms_web.widgets.django import ModelFormWidget
from pyforms_web.organizers import no_columns, segment
from reagents.models import Virus
from reagents.models.virus_type import VirusType


class VirusForm(ModelFormWidget):
    

    MODEL = Virus
    
    TITLE = 'Virus editor'

    FIELDSETS = [
        ('virus_name', 'contact', 'lab'),
        'supplier',
        segment(
            ('virus_reference', 'virus_type', 'virus_serotype'),
            ('virus_titter', 'virus_dna_available'),
        )
    ]
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ########################################################



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.virus_type.changed_event = self.__virus_type_changed_evt
        self.virus_serotype.hide()

    def __virus_type_changed_evt(self):
        try:
            obj = VirusType.objects.get(pk=self.virus_type.value)
        except VirusType.DoesNotExist:
            self.virus_serotype.hide()
            return

        if obj.virustype_name == "AAV":
            self.virus_serotype.show()
        else:
            self.virus_serotype.hide()


    