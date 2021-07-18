from django.db import models


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='News')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True, verbose_name='Created Date')
    update_date = models.DateTimeField(auto_now_add=True, verbose_name='Update Date')
    published = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-update_date']

    def __str__(self):
        return self.title
