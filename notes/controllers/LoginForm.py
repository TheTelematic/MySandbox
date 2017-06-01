from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="User", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


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

    else:

        return LoginForm()

