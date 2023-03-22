from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from blogs.models import Blogs
from .forms import BlogForm


class PostsDetail(DetailView):
    queryset = Blogs.objects.all()
    template_name = 'main/gallery.html'


class CreatePost(CreateView):
    form_class = BlogForm
    template_name = 'main/createPost.html'
    model = Blogs


def delete(request, pk):
    post = Blogs.objects.get(pk=pk)
    post.delete()
    return redirect('/')
