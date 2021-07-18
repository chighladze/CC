from django.urls import path
from django.conf.urls import url
from news.views import *

urlpatterns = [
    path('', news, name='news'),
    path('add-news/', add_news, name='add_news'),
    path('create/', create, name='create'),
    path('detail/<int:news_id>/', detail, name='detail'),

]
