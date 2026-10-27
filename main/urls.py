from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    # path('read', views.read, name='read'),
]