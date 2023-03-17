from django.shortcuts import render, redirect
from django.views.generic import DetailView
from blogs.models import Blogs


class PostsDetail(DetailView):
    queryset = Blogs.objects.all()
    template_name = 'main/gallery.html'


def delete(request, pk):
    post = Blogs.objects.get(pk=pk)
    post.delete()
    return redirect('/')
