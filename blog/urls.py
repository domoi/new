from django.urls import path,include
from django.views.generic import TemplateView
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('category/<slug:slug>/', Show_one.as_view(), name='blog'),
    path('new/', addpage, name='new'),
]