# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from notes.controllers.IndexCtr import IndexCtr


def index(request):
    """
            Index of the app
        :param request: HttpRequest
        :return: response: HttpResponse
        """
    return IndexCtr(request=request).get_http_response()
