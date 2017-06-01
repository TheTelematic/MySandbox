from datetime import datetime, timedelta

from django.contrib import auth

from MySandbox import settings


class SessionCtr:
    def __init__(self):
        pass

    @staticmethod
    def process_request(request):

        """try:
            last_activity = request.session['username']

            # return True
        except KeyError:
            print "KeyError - 0001"
            return False

        now = datetime.now()

        if (now - last_activity).minute > 10:

            request.session.flush()

            return False

        if not request.is_ajax():
            # don't set this for ajax requests or else your
            # expired session checks will keep the session from
            # expiring :)
            request.session['last_activity'] = now

            return True"""
        if not request.user.is_authenticated():
            # Can't log out if not logged in
            return

        try:
            if datetime.now() - request.session['last_touch'] > timedelta(0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError:
            pass

        request.session['last_touch'] = datetime.now()

