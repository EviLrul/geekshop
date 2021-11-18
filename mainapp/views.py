from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'geekshop - Товар',
    }
    return render(request, 'mainapp/products.html', context)


def test(request):
    cont = {
        'title': 'GeekShop',
        'header': 'Всем привет!',
        'user': 'Serg',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 5600},
        ]
    }
    return render(request, 'test_page.html', cont)
