from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogListView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model=Post
    template_name = 'post_new'
    fields = ['title', 'author', 'body']
        