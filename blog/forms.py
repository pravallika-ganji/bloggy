from blog.models import *

from django import forms

from django.contrib.auth.models import User

choices = Category.objects.all().values_list('name','name')

choice_list = []
for i in choices:
	choice_list.append(i)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title","category","user","image","description"]
		widgets = {
		"title":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Blog title",
			}),
		"category":forms.Select(choices=choice_list,attrs={
			"class":"form-control my-2",
			"placeholder":"select",
			}),
		"user":forms.TextInput(attrs={
			"class":"form-control my-2",
			"value":"",
			"id":'elder',
			"type":'hidden'
			}),
		"description":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Write your description here.",
			# "rows":8,
			}),
		}

class EditPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title","category","image","description"]
		widgets = {
		"title":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Blog title",
			}),
		"category":forms.Select(choices=choice_list,attrs={
			"class":"form-control my-2",
			"placeholder":"select",
			}),
		"description":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Write your description here.",
			"rows":8,
			}),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ["name","comment"]
		widgets = {
		"name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter name",
			}),
		"comment":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Write your comment here.",
			# "rows":8,
			}),
		}
