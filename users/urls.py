from django.conf import settings
from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('register/', usersignup, name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user,name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate_account, name='activate'),
    path('email/', email_confirm, name='email_confirm'),
    path('email_success/', success, name='success'),
    path('change_profile/<int:pk>/', Change_profile.as_view(), name='change_profile'),
    path("", include("allauth.urls")), #most important
]
