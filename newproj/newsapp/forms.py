from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    publish_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    class Meta:
        model = Article
        fields = ['title', 'content', 'publish_date']