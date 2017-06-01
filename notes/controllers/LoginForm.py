from django import forms

from notes.models import User
from notes.strings import ERROR_USER_NOT_EXIST, LOGIN_OK, ERROR_PASSWORD_INCORRECT, EMPTY_LOGIN_FORM


class LoginForm(forms.Form):
    username = forms.CharField(label="User", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100)


def get_login(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            query = User.objects.filter(username=username)

            if not query:
                return ERROR_USER_NOT_EXIST

            print query
            correct = query.first().password

            print correct

            print "Given password: " + password
            print "Correct password : " + correct

            if correct != password:
                return ERROR_PASSWORD_INCORRECT

            request.session['username'] = username
            request.session['password'] = password

            print "User connected:" + request.session['username']

            return LOGIN_OK
        else:
            print "Form not valid"

            return EMPTY_LOGIN_FORM

    else:
        print "Login form via GET"
        return EMPTY_LOGIN_FORM


def get_empty_form():
    return LoginForm()


