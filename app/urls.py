from django.contrib import admin
from django.urls import path
from app.views import *

app_name='app'

urlpatterns=[
    path('home/',home,name='home'),
    path('about/',about,name='about')
]