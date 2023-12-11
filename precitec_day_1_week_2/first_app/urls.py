from django.contrib import admin
from django.urls import path , include

from first_app.views import home
urlpatterns = [
   path('',home, name='home'),
]
