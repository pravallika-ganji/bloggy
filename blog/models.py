from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    propic = models.ImageField(upload_to = 'blogimages/profile',blank=True)
    website_url = models.CharField(max_length=200, unique=True,blank=True)
    fb_url = models.CharField(max_length=200, unique=True,blank=True)
    instagram_url = models.CharField(max_length=200, unique=True,blank=True)
    linkedin_url = models.CharField(max_length=200, unique=True,blank=True)

    def __str__(self):
        return str(self.user)

    def gey_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    # approval = models.BooleanField(default=False)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'blogimages/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    category = models.CharField(max_length = 255, default='coding')
    likes = models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):      
        return self.title + ' | ' +str(self.user)
        
    def gey_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    comment = models.TextField()
    commented_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.post.title
