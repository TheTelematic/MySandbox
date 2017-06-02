from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from notes import constants
from notes.controllers.SessionCtr import SessionCtr
from notes.strings import INDEX_PAGE


class MainCtr(SessionCtr):
    def __init__(self, request, stylesheets=[], scripts=[], sessionRequired=True):
        """
            Initialize the header of the html file, and check if the session is expired
        :param request: HttpRequest
        :param stylesheets: Additional stylesheets used for the body
        :param scripts: Additional scripts used for the body
        """

        SessionCtr.__init__(self)

        if sessionRequired and not self.process_request(request):
            HttpResponseRedirect(INDEX_PAGE)

        template_header = loader.get_template(constants.html_header)
        template_footer = loader.get_template(constants.html_footer)
        context = {
            'stylesheets': stylesheets + [constants.css_header, ],
            'scripts': scripts,
            'favicon': constants.img_favicon,

        }

        self.__header = template_header.render(context, request)
        self.__nav = ""
        self.__aside = ""
        self.__section = ""
        self.__footer = template_footer.render({'aboutme': 'aboutme/'}, request)

    """
        Protected Methods
    """
    def add_section(self, section):
        """
            Add the body
        :param section: The section of the body
        :return: 
        """
        self.__section = section

    def add_aside(self, aside):
        """
            Add the body
        :param aside: The aside of the body
        :return: 
        """
        self.__aside = aside

    def add_nav(self, nav):
        """
            Add the body
        :param nav: The nav of the body
        :return: 
        """
        self.__nav = nav

    """
        Public API
    """
    def get_http_response(self):

        return HttpResponse(self.__header + self.__nav + self.__aside + self.__section + self.__footer)



