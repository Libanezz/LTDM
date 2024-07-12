from django.urls import path
from . import views


urlpatterns=[
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('ropadehombre', views.ropadehombre, name='ropadehombre'),
    path('ropademujer', views.ropadehombre, name='ropademujer'),
    path('joyeria', views.joyeria, name='joyeria'),


]