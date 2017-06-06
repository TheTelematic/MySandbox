# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect

from notes.controllers.AboutMeCtr import AboutMeCtr
from notes.controllers.IndexCtr import IndexCtr
from notes.controllers.LogoutCtr import LogoutCtr
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

        return redirect('/notes/wall/')
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
        return redirect('/notes/wall/')
    else:
        return register_handler.get_http_response()


def aboutme(request):
    """
        See the page about me
    :param request: HttpRequest
    :return: HttpResponse
    """

    return AboutMeCtr(request=request).get_http_response()


def logout(request):
    """
        Logout
    :param request: HttpRequest
    :return: HttpResponse
    """
    LogoutCtr(request)
    return redirect('/notes/')
