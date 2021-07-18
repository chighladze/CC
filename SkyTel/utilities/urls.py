from django.urls import path
from django.conf.urls import url
from utilities.views import *

urlpatterns = [
    path('ping/', ping, name='ping'),
    path('traceroute/', traceroute, name='traceroute'),

]