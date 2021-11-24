from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'geekshop | Авторизация',    }
    return render(request, 'authapp/login.html', context)

def registr(request):
    context = {
        'title': 'geekshop | Регистрация',    }
    return render(request, 'authapp/register.html', context)