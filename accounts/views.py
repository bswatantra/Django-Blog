from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.


def login(request):
    if request.method == 'POST':
        # email = request.POST['email']
        # password = request.POST['password']
        pass
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create(
            username=username, email=email, password=password
        ).user.save()
    else:
        return render(request, 'accounts/register.html')
