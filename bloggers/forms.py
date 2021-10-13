from blog.models import *
from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm

class RegisterForm(UserCreationForm):
	password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
	password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","password1","password2"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter firstname",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter lastname",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter email address",
			}),
		}

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter firstname",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter lastname",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter email address",
			}),
		}

class PasswordChangingForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
	new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
	new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

	class Meta:
		model = User
		fields = ('old_password','new_password2','new_password1')


class ProfilePageForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio','propic','website_url','fb_url','instagram_url','linkedin_url')
		widgets = {
					"bio":forms.Textarea(attrs={
					"class":"form-control my-2",
					"placeholder":"Enter bio here",
				}),
					"website_url":forms.TextInput(attrs={
					"class":"form-control my-2",
					"placeholder":"Enter bio here",
				}),
					"fb_url":forms.TextInput(attrs={
					"class":"form-control my-2",
					"placeholder":"Enter bio here",
				}),
					"instagram_url":forms.TextInput(attrs={
					"class":"form-control my-2",
					"placeholder":"Enter bio here",
				}),
					"linkedin_url":forms.TextInput(attrs={
					"class":"form-control my-2",
					"placeholder":"Enter bio here",
				}),

		}

class EditProfilePageForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio','propic','website_url','fb_url','instagram_url','linkedin_url')
		widgets = {
					"bio":forms.Textarea(attrs={
					"class":"form-control my-2",
					"placeholder":"Enter bio here",
				}),
					"website_url":forms.TextInput(attrs={
					"class":"form-control my-2",
					"placeholder":"Enter bio here",
				}),
					"fb_url":forms.TextInput(attrs={
					"class":"form-control my-2",
					"placeholder":"Enter bio here",
				}),
					"instagram_url":forms.TextInput(attrs={
					"class":"form-control my-2",
					"placeholder":"Enter bio here",
				}),
					"linkedin_url":forms.TextInput(attrs={
					"class":"form-control my-2",
					"placeholder":"Enter bio here",
				}),

		}

