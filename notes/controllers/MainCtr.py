from django.http import HttpResponse
from django.template import loader

from notes import constants


class MainCtr:
    def __init__(self, request, stylesheets=None, scripts=None):
        """
            Initialize the header of the html file
        :param request: HttpRequest
        :param stylesheets: Additional stylesheets used for the body
        :param scripts: Additional scripts used for the body
        """
        template_header = loader.get_template(constants.html_header)

        context = {
            'stylesheets': stylesheets,
            'scripts': scripts,
        }

        self.__output = template_header.render(context, request)

    """
        Protected Methods
    """
    def add_output(self, output):
        self.__output += output

    """
        Public API
    """
    def get_httpresponse(self):
        return HttpResponse(self.__output)



