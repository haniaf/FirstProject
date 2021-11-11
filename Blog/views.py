from django.shortcuts import render, get_object_or_404, reverse
from .models import Article
from .forms import BlogForm

from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)
class ArticleListView(ListView):
    template_name = "Blog/article_list.html"
    queryset = Article.objects.all()

class ArticleCreateView(CreateView):
    template_name = "Blog/article_create.html"
    queryset = Article.objects.all()
    form_class = BlogForm
    def form_valid(self, form):
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    template_name = "Blog/article_detail.html"
    queryset = Article.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = "Blog/article_update.html"


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'Blog/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('Blog:article-list')



