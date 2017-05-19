from django.shortcuts import render

from notes import constants
from notes.controllers import LoginForm
from notes.controllers.MainCtr import MainCtr


class IndexCtr(MainCtr):
    def __init__(self, request):
        MainCtr.__init__(self, request)

        self.request = request

    def is_logged(self):
        result = LoginForm.get_login(self.request)

        if result is "1":
            print "Logged"
            return True
        else:
            print "NOT logged"
            self.add_section(render(self.request, constants.html_login, {'form': result}).content)




