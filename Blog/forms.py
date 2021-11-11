from django.db import models
from django import forms
from .models import Article

class BlogForm(forms.ModelForm):
    title = models.CharField()
    content = models.TextField()
    active = models.BooleanField()
    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "active",
        ]