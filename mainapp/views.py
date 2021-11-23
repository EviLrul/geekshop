from django.shortcuts import render
from mainapp.models import Product

import json
import os



MODULE_DIR = os.path.dirname(__file__)
# Create your views here.


def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'geekshop - Товары',
        # 'products': [
        #     {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090, 'about': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', 'pic': 'vendor/img/products/Adidas-hoodie.png'},
        #     {'name': 'Синяя куртка The North Face', 'price': 23725, 'about': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.', 'pic': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
        #     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390, 'about': 'Материал с плюшевой текстурой. Удобный и мягкий.', 'pic': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
        #     {'name': 'Черный рюкзак Nike Heritage', 'price': 2340, 'about': 'Плотная ткань. Легкий материал.', 'pic': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
        #     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590, 'about': 'Гладкий кожаный верх. Натуральный материал.', 'pic': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
        #     {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890, 'about': 'Легкая эластичная ткань сирсакер Фактурная ткань.', 'pic': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
        # ]
        #'products': json.load((open(file_path, encoding='utf-8')))
        'products': Product.objects.all()
    }

    #context['products'] = json.load((open(file_path, encoding='utf-8')))
    return render(request, 'mainapp/products.html', context)
