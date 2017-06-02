from django.shortcuts import render

from notes import constants
from notes.controllers.MainCtr import MainCtr


class AboutMeCtr(MainCtr):
    def __init__(self, request):
        MainCtr.__init__(self, request, stylesheets=["css/register.css", ], scripts=["js/register.js"], sessionRequired=False)

        self.request = request

        self.add_section(render(self.request, constants.html_aboutme).content)

