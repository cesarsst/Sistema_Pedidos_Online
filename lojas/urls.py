from django.contrib import admin
from django.urls import path
from lojas.views import index_lojas, details


urlpatterns = [
    path('', index_lojas, name='index_lojas'),
    path('<slug:slug>', details, name='details'),
]