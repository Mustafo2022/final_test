from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import DetailView, CreateView, ListView

import blogs.models
from blogs.models import Blogs
from .forms import BlogForm


class PostsDetail(DetailView):
    queryset = Blogs.objects.all()
    template_name = 'main/detail.html'


class CreatePost(CreateView):
    form_class = BlogForm
    template_name = 'main/createPost.html'
    model = Blogs


def GalleryLike(request, pk):
    post = get_object_or_404(Blogs, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    context = {
        'liked': liked
    }
    return redirect('gallery')


def PostLike(request, pk):
    post = get_object_or_404(Blogs, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    context = {
        'liked': liked
    }
    return HttpResponseRedirect('/', context)


def GalleryDelete(request, pk):
    post = Blogs.objects.get(pk=pk)
    post.delete()
    return redirect('gallery')


def delete(request, pk):
    post = Blogs.objects.get(pk=pk)
    post.delete()
    return redirect('/')


def BlogCreate(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()

            return redirect('/')

    return render(request, 'main/createPost.html', {'form': form})


class BlogListView(ListView):
    template_name = 'main/gallery.html'

    def get_queryset(self):
        qs = Blogs.objects.all()
        sort = self.request.GET.get('sort', '')
        if sort:
            qs = qs.order_by(sort)

        return qs
