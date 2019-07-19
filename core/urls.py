from django.contrib import admin
from django.urls import path

from core.views import contact, home


urlpatterns = [
    path('contact/', contact, name='contato'),
    path('', home, name='home'),

]