from django.shortcuts import render
from django.template import loader

from notes import constants
from notes.controllers import NoteForm
from notes.controllers.MainCtr import MainCtr


class WallCtr(MainCtr):
    def __init__(self, request):
        MainCtr.__init__(self, stylesheets=[constants.css_wall], scripts=[constants.js_wall], request=request)

        template = loader.get_template(constants.html_wall)

        context = {
            'username': request.session['username']
        }

        self.request = request

        self.add_section(template.render(context, request))
        self.add_aside(render(request, constants.html_wall_aside).content)

    def new_note(self):

        result = NoteForm.add(self.request)

        context = {'form': result}
        self.add_section(render(self.request, constants.html_register, context=context).content)
