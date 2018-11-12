# -*- coding: utf-8 -*-
from django import forms
from models import Fault, FaultComment
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Hasło',
							 	widget=forms.PasswordInput)
	password2 = forms.CharField(label='Powtórz hasło:',
								widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Hasła są identyczne.')
			return cd['password2']


class EditFaultForm(forms.Form):
	status_choice = (
        ('reported', 'Zgloszone'),
        ('in_progress', 'W trakcie'),
        ('done', 'Naprawione'),
    )
	status_usterki = forms.ChoiceField(choices=status_choice)
	
		
class FaultCommentForm(forms.ModelForm):
	class Meta:
		model = FaultComment
		fields = ['fault', 'body']