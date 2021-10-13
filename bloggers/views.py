from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404,reverse
from django.views import generic 
from django.views.generic import DetailView,UpdateView,CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm,EditProfileForm,PasswordChangingForm,ProfilePageForm,EditProfilePageForm
from django.contrib.auth.views import *
from blog.models import Profile
from blog.forms import *
# Create your views here.

class CreateProfilePageView(CreateView):
	form_class = ProfilePageForm
	template_name = 'registration/createuser.html'
	success_url = reverse_lazy('home')

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class ShowProfileView(DetailView):
	model = Profile
	template_name= "registration/userprof.html"

	def get_context_data(self,*args,**kwargs):
		users = Profile.objects.all()
		user = self.request.user
		p = Post.objects.filter(user=user)
		context = super(ShowProfileView,self).get_context_data(*args,**kwargs)
		page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
		context['page_user'] = page_user
		context['posts'] = p
		return context

class EditProfileView(UpdateView):
	form_class = EditProfilePageForm
	template_name = 'registration/edituser.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user.profile


class UserRegisterView(generic.CreateView):
	form_class = RegisterForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/editprofile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user

class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	success_url = reverse_lazy('pwdsucc')
	template_name = 'registration/changepwd.html'

def PasswordSuccess(request):
	return render(request,'registration/pwdsucc.html',{})


