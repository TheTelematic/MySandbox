from django import forms


class NoteForm(forms.Form):
    content = forms.Textarea()


def add(request):

    return NoteForm()
