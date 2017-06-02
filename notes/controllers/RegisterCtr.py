from django.shortcuts import render

from notes import constants
from notes.controllers import RegisterForm
from notes.controllers.MainCtr import MainCtr
from notes.strings import REGISTER_OK, ERROR_EXISTING_USER, EMPTY_REGISTER_FORM, ERROR_PASSWORD_IS_EMPTY, \
    MESSAGE_ERROR_PASSWORD_IS_EMPTY, MESSAGE_ERROR_EXISTING_USER, ERROR_USER_IS_EMPTY, MESSAGE_ERROR_USER_IS_EMPTY


class RegisterCtr(MainCtr):
    def __init__(self, request, error=None):
        MainCtr.__init__(self, request, stylesheets=["css/register.css", ], scripts=["js/register.js"], sessionRequired=False)

        self.request = request

    def register(self):

        result = RegisterForm.register(self.request)

        if result is REGISTER_OK:
            print "result == REGISTER_OK"
            return True
        elif result is ERROR_EXISTING_USER:
            print "result == ERROR_EXISTING_USER"
            context = {'form': RegisterForm.get_empty_form(),
                       'error': MESSAGE_ERROR_EXISTING_USER}
            self.add_section(render(self.request, constants.html_register, context=context).content)
            return False

        elif result is ERROR_USER_IS_EMPTY:
            print "result == ERROR_USER_IS_EMPTY"
            context = {'form': RegisterForm.get_empty_form(),
                       'error': MESSAGE_ERROR_USER_IS_EMPTY}
            self.add_section(render(self.request, constants.html_register, context=context).content)
            return False

        elif result is ERROR_PASSWORD_IS_EMPTY:
            print "result == ERROR_PASSWORD_IS_EMPTY"
            context = {'form': RegisterForm.get_empty_form(),
                       'error': MESSAGE_ERROR_PASSWORD_IS_EMPTY}
            self.add_section(render(self.request, constants.html_register, context=context).content)
            return False

        elif result is EMPTY_REGISTER_FORM:
            print "result == EMPTY_REGISTER_FORM"
            context = {'form': RegisterForm.get_empty_form()}
            self.add_section(render(self.request, constants.html_register, context=context).content)
            return False



        else:
            print "NO DEBERIA PASAR POR AQUI"
            return None
