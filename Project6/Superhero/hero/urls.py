from django.urls import path, include
from .views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [

    path('',                HeroListView.as_view(),    name='hero_list'),
    path('<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('add',             HeroCreateView.as_view(),  name='hero_add'),
    path('<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
