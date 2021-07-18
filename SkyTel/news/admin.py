from django.contrib import admin
from news.models import News




class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'update_date', 'published')
    list_display_links = ('id', 'title')



admin.site.register(News, NewsAdmin)