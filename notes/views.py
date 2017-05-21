# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from notes.controllers.IndexCtr import IndexCtr
from notes.controllers.WallCtr import WallCtr


def index(request):
    """
            Index of the app
        :param request: HttpRequest
        :return: response: HttpResponse
        """
    index = IndexCtr(request=request);

    if index.is_logged():
        return wall(request)
    else:
        return index.get_http_response()


def wall(request):
    """
            Index of the app
        :param request: HttpRequest
        :return: response: HttpResponse
        """
    return WallCtr(request=request).get_http_response()
