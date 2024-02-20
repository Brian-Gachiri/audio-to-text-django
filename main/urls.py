
from django.contrib import admin
from django.urls import path

from main.views import index, uploadFile

urlpatterns = [
    path('', index, name='index'),
    path('upload', uploadFile, name='upload')
]
