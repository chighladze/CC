from django.urls import path
from django.conf.urls import url
from myApp.views import *

urlpatterns = [
    path('', index, name='home'),
    path('monthly/', monthly_st_desk, name='monthly_st_desk'),
    # path('monthly/filter/', monthly_st_desk_filter, name="monthly_filter"),
]
