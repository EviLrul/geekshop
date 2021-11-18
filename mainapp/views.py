from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'geekshop - Товары',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Синяя куртка The North Face', 'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890},
        ]
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
