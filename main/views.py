from django.shortcuts import render
from blogs.models import Blogs
from django.views.generic import DetailView


def HomeView(request):
    blogs = Blogs.objects.all()
    return render(request, 'main/index.html', {'blogs': blogs})


