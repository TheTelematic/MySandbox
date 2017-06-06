from datetime import datetime, timedelta

from django.contrib import auth

from MySandbox import settings


class SessionCtr:
    def __init__(self):
        pass

    @staticmethod
    def process_request(request):

        if not request.user.is_authenticated():
            # Can't log out if not logged in
            return

        try:
            if datetime.now() - request.session['last_touch'] > timedelta(0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                return SessionCtr.logout(request)

        except KeyError:
            pass

        request.session['last_touch'] = datetime.now()

    @staticmethod
    def logout(request):
        auth.logout(request)
        request.session.pop('username', None)
        return
