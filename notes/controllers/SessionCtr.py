from datetime import datetime


class SessionCtr:
    def __init__(self):
        pass

    @staticmethod
    def process_request(request):

        try:
            last_activity = request.session['last_activity']

        except KeyError:
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

            return True

