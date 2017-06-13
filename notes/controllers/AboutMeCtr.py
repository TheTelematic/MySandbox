from django.shortcuts import render

from notes import constants
from notes.controllers.MainCtr import MainCtr


class AboutMeCtr(MainCtr):
    def __init__(self, request):
        MainCtr.__init__(self, request, stylesheets=[constants.css_aboutme, ], sessionRequired=False)

        self.add_section(render(request, constants.html_aboutme).content)
        self.add_aside(render(request, constants.html_aboutme_aside).content)


