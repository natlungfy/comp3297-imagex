from django import forms
from search.models import Member


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    description = forms.CharField(max_length=280, label='Description')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.description = self.cleaned_data['description']
        user.save()

        member = Member(username=user)
        member.save()
