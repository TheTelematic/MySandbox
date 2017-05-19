from django.template import loader

from notes import constants


class MainCtr:
    def __init__(self, request, stylesheets=None, scripts=None):
        """
            Initialize 
        :param request: 
        :param stylesheets: 
        :param scripts: 
        """
        template_header = loader.get_template(constants.html_header)

        context = {
            'stylesheets': stylesheets,
            'scripts': scripts,
        }

        self.__output = template_header.render(context, request)




