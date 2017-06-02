from django import forms

from notes.models import User
from notes.strings import REGISTER_OK, ERROR_EXISTING_USER, EMPTY_REGISTER_FORM, ERROR_PASSWORD_IS_EMPTY, \
    ERROR_USER_IS_EMPTY


class RegisterForm(forms.Form):
    username = forms.CharField(label="User", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100)


def register(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if username == "":
                return ERROR_USER_IS_EMPTY

            if password == "":
                return ERROR_PASSWORD_IS_EMPTY

            query = User.objects.filter(username=username)
            print query

            if query:
                return ERROR_EXISTING_USER




            request.session['username'] = username
            request.session['password'] = password

            # print "DEBUG: User-> {} Password-> {}".format(username, password)

            user = User(username=username, password=password)

            user.save()

            return REGISTER_OK
        else:
            print "Register form not valid"

            return EMPTY_REGISTER_FORM

    else:
        print "Register form via GET"

        return RegisterForm()


def get_empty_form():
    return RegisterForm()


