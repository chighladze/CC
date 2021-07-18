from django import forms
from .models import News


class NewsForm(forms.Form):
    title = forms.CharField(max_length=50, label='News Name')
    content = forms.CharField(label='Enter Text', required=True)
    published = forms.BooleanField(label='Published', initial=True)


class MyNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content')

