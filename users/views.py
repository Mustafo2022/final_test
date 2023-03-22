import random
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import ResetPassword
from .forms import RegistrationForm
from django.contrib import messages


def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        # emails = UserModel.objects.all().filter(email=email)
        # if emails:
        title = 'KiddZo'
        x = []
        six = ['1', '2', '3', '4', '5', '6']
        for i in range(random.randrange(5, 6)):
            rand = random.randrange(99999, 1000000)
            list(str(rand))
            x = rand

        msg = f'Thank you for using our app! Your recovery password is {x}'
        send_mail(title, msg, 'trendy2022.asus@gmail.com', [email])
        return redirect('login')
    return render(request, 'login/forgot-pass.html')


# def sendPassword(request):
#     mail = 'trendy2022.asus@gmail.com'
#     title = 'KiddZo'
#     x = []
#     six = ['1', '2', '3', '4', '5', '6']
#     for i in six:
#         rand = random.randrange(99999, 1000000)
#         list(str(rand))
#         x = rand
#
#
#     msg = f'Thank you for using our app! Your recovery password is {x}'
#     send_mail(title, msg, 'wosit90263@etondy.com', [mail])
#     return redirect('login')


def logoutView(request):
    logout(request)
    return redirect('login')


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'login/index.html')


def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.SUCCESS, 'This user name was already taken!')
    return render(request, 'login/create.html', {'form': form})
