from django.contrib import admin
from django.urls import path
from .views import Helloworld

urlpatterns = [
    path('',Helloworld , name='home'),

]