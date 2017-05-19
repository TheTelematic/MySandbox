from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from notes import constants


class LoginForm(forms.Form):
    username = forms.CharField(label="User", max_length=100)

    def __init__(self):
        super(LoginForm, self).__init__()


def get_login(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            # TODO: Pick up the user data
            request.session['username'] = form.cleaned_data['username']

            print "User connected:" + request.session['username']

            return "1"
        else:
            print "Form not valid"

            return LoginForm()
            #form = ()
            #return render(request, constants.html_login, {'form': form}).content

    else:
        #  print "HHHHEEEEEEEEEEEEEEEEEEEEEEEEEEEE"

        return LoginForm()

