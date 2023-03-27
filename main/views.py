import random

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from blogs.models import Blogs
from users.models import UserModel
from .forms import ContactForm
from .models import Messages


def HomeView(request):
    blogs = Blogs.objects.all().order_by('-id')[:50]
    print("blogs")
    return render(request, 'main/index.html', {'blogs': blogs})


class ContactView(CreateView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = 'contact/'
    model = Messages


def AboutView(request):
    users = UserModel.objects.all().order_by('popularity')[:5]
    return render(request, 'main/about.html', {'users': users})


def verify(request):
    if not request.user.email_verified:
        request.user.email_verified = True
        request.user.points += 15

        email = request.user.email
        title = 'KiddZo'
        x = []
        for i in range(random.randrange(5, 6)):
            rand = random.randrange(99999, 1000000)
            list(str(rand))
            x = rand

        msg = f'Thank you for using our app! Your password for verify email  is {x}'
        send_mail(title, msg, 'trendy2022.asus@gmail.com', [email])

        blogs = Blogs.objects.all().order_by('-id')[:50]
        return render(request, 'main/index.html', {'blogs': blogs})
    else:
        return redirect('/')


def AddPoint(request):
    request.user.points -= 15
    return redirect('/')
