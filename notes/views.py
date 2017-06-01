# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from notes.controllers.IndexCtr import IndexCtr
from notes.controllers.RegisterCtr import RegisterCtr
from notes.controllers.WallCtr import WallCtr


def index(request):
    """
            Index of the app, redirect to the wall or to the login page
        :param request: HttpRequest
        :return: response: HttpResponse
    """
    index_handler = IndexCtr(request=request)

    if index_handler.is_logged():
        return wall(request)
    else:
        return index_handler.get_http_response()


def wall(request):
    """
            The wall of the user
        :param request: HttpRequest
        :return: response: HttpResponse
    """
    return WallCtr(request=request).get_http_response()


def register(request, error=None):
    """
        The register page
    :param error: Error registering a user
    :param request: HttpRequest
    :return: HttpResponse
    """

    register_handler = RegisterCtr(request=request, error=error)

    if register_handler.register():
        print "REGISTRO CORRECTO"
        return wall(request)
    else:
        return register_handler.get_http_response()


