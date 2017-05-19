from django.template import loader

from notes import constants
from notes.controllers.MainCtr import MainCtr


class IndexCtr(MainCtr):
    def __init__(self, request):
        MainCtr.__init__(self, request)

        template = loader.get_template(constants.html_index)

        context = {

        }

        self.add_section(template.render(context, request))


