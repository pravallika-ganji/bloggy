from django.shortcuts import render,redirect,get_object_or_404
from blog.models import *
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy
# Create your views here.

def home(request):
	p = Post.objects.all()
	c = Category.objects.all()
	context = {'posts': p , 'c':c}
	return render(request,'home.html',context)

def homee(request):
	c = Category.objects.all()
	context = {'c':c}
	return render(request,'navbar.html',context)

class AddCommentView(CreateView):
	form_class = CommentForm
	template_name = 'addcomment.html'
	success_url = ('/')

	def form_valid(self,form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)



def CategoryListView(request):
	c = Category.objects.all()
	context = {'c':c}
	return render(request,'catlist.html',context)

class ArticleView(LoginRequiredMixin,DetailView):
	login_url='login'
	model = Post
	template_name = 'detail.html'
	def get_context_data(self,*args,**kwargs):
		context = super(ArticleView,self).get_context_data(*args,**kwargs)
		stuff = get_object_or_404(Post,id=self.kwargs['pk'])
		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked=True
		total_likes = stuff.total_likes()
		context['total_likes'] = total_likes
		context['liked'] = liked
		return context

def CategoryView(request,cats):
	category_posts = Post.objects.filter(category=cats.replace('-'," "))
	return render(request, 'category.html', {'cats':cats.title().replace('-'," "),'category_posts':category_posts})

class PostCreate(LoginRequiredMixin,CreateView):
	login_url='login'
	model = Post
	form_class=PostForm
	template_name = 'createpost.html'
	success_url = reverse_lazy('home')

class CategoryCreate(CreateView):
	model = Category
	template_name = 'createcat.html'
	fields= "__all__"
	

def PostUpdate(request,m):
	k = Post.objects.get(id=m)
	if request.method == "POST":
		e = PostForm(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Blog Updated Successfully".format(k.title))
			return redirect('/')
	e = PostForm(instance=k)
	return render(request,'update.html',{'x':e,'k':k})

def PostDelete(request,n):
	v = Post.objects.get(id=n)
	if request.method == "POST":
		v.delete()
		messages.info(request,"{} BLog Deleted Successfully".format(v.title))
		return redirect('/')
	return render(request,'delete.html',{'q':v})

def LikeView(request,pk):
	post = get_object_or_404(Post,id=request.POST.get('post_id'))
	liked = False 
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked=False
	else:
		post.likes.add(request.user)
		liked=True
	return HttpResponseRedirect(reverse('detail',args=[str(pk)]))

def searchView(request):
	if request.method == "POST":
		searched = request.POST['searched']
		p = Post.objects.filter(title__icontains=searched,description__icontains=searched)
		return render(request,'search.html',{'posts':p})
	else:
		return render(request,'search.html',{})


	
