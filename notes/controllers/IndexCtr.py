from django.shortcuts import render

from notes import constants
from notes.controllers import LoginForm
from notes.controllers.MainCtr import MainCtr
from notes.strings import LOGIN_OK, ERROR_PASSWORD_INCORRECT, ERROR_USER_NOT_EXIST, EMPTY_LOGIN_FORM, \
    MESSAGE_ERROR_PASSWORD_INCORRECT, MESSAGE_ERROR_USER_NOT_EXIST


class IndexCtr(MainCtr):
    def __init__(self, request):
        MainCtr.__init__(self, request, stylesheets=["css/index.css", "css/login.css", ])

        self.request = request

    def is_logged(self):
        result = LoginForm.get_login(self.request)

        if result is LOGIN_OK:
            print "Logged"
            return True

        elif result is ERROR_USER_NOT_EXIST:
            print ERROR_USER_NOT_EXIST
            context = {
                'form': LoginForm.get_empty_form(),
                'error': MESSAGE_ERROR_USER_NOT_EXIST
            }
            self.add_section(render(self.request, constants.html_login, context=context).content)
            return False

        elif result is ERROR_PASSWORD_INCORRECT:
            print ERROR_PASSWORD_INCORRECT
            context = {
                'form': LoginForm.get_empty_form(),
                'error': MESSAGE_ERROR_PASSWORD_INCORRECT
            }
            self.add_section(render(self.request, constants.html_login, context=context).content)
            return False

        elif result is EMPTY_LOGIN_FORM:
            print EMPTY_LOGIN_FORM
            context = {
                'form': LoginForm.get_empty_form(),
            }
            self.add_section(render(self.request, constants.html_login, context=context).content)
            return False

        else:
            print "POR AQUI NO DEBERIA PASAR"
            return None



