from bloggers.views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('register/',UserRegisterView.as_view(),name = "register"),
        path('editprofile/',UserEditView.as_view(),name = "editprofile"),
        path('pwd/',PasswordsChangeView.as_view(),name="change"),
        path('pwdsuccess/',PasswordSuccess,name="pwdsucc"),
        path('<int:pk>/profile/',ShowProfileView.as_view(),name="profile"),
        path('<int:pk>/editprofile/',EditProfileView.as_view(),name="edituserprofile"),
        path('createprofile/',CreateProfilePageView.as_view(),name="createuserprofile"),
        path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/passwordreset.html',
             # success_url='/login/'
         ),
         name='password-reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/passwordresetdone.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/passwordresetconfirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/passwordresetcomplete.html'
         ),
         name='password_reset_complete'),
]