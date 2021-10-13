from blog.views import *
from django.urls import path
from django.contrib.auth import views as v

urlpatterns = [
    path('',home,name="home"),
    path('article/<int:pk>',ArticleView.as_view(), name = "detail"),
    path('createpost/',PostCreate.as_view(),name="create"),
    path('postupdate/<int:m>',PostUpdate,name="update"),
    path('postdelete/<int:n>',PostDelete,name="delete"),
    path('createcat/',CategoryCreate.as_view(),name="createcat"),
    path('category/<str:cats>/',CategoryView,name="category"),
    path('category/',CategoryListView,name="catlist"),
    path('likes/<int:pk>',LikeView,name='like'),
    path('article/<int:pk>/comment/',AddCommentView.as_view(),name="comment"),
    path('search/',searchView,name="search"),
]