from notes.controllers.MainCtr import MainCtr


class LogoutCtr(MainCtr):
    def __init__(self, request):
        MainCtr.__init__(self, request, sessionRequired=False)

        self.logout(request)

        print "Logout"


