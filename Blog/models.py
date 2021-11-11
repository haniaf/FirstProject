from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("Blog:article-detail", kwargs={"id": self.id})

