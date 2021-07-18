import os

from django.shortcuts import render, redirect
from news.models import News
from .forms import NewsForm, MyNewsForm


# Create your views here.


def news(request):
    if request.method == 'POST':
        pk = int(request.POST['_method'])
        News.objects.filter(pk=pk).delete()
    item = News.objects.filter(published=True)
    context = {
        'item': item,
    }
    return render(request, 'news/news.html', context=context)


def add_news(request):
    form = NewsForm()
    return render(request, 'news/add_news.html', context={'form': form})


# def create(request):
#     # if form.is_valid():
#     title = request.POST['title']
#     content = request.POST['content']
#     if request.POST['published'] == "on":
#         published = True
#     else:
#         published = False
#     News.objects.create(title=title, content=content, published=published)
#     return redirect(news)


def create(request):
    if request.method == "POST":
        form = MyNewsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST['published'] == "on":
                form.published = True
            else:
                form.published = False
            form.save()
            # News.objects.create(title=title, content=content, published=published)
        else:
            print(form.errors)
            return render(request, 'news/add_news.html', context={'form': form})
    return redirect(news)


def detail(request, news_id):
    item = News.objects.filter(pk=news_id)
    context = {
        'item': item,
    }
    return render(request, 'news/news_detail.html', context=context)



