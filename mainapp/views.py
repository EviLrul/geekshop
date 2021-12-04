from django.shortcuts import render
from django.views.generic import DetailView

from mainapp.models import Product, ProductCategory

import json
import os

MODULE_DIR = os.path.dirname(__file__)
# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    # file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'geekshop | Товары',

        #'products': json.load((open(file_path, encoding='utf-8')))
        'products': Product.objects.all(),
        'categoreis': ProductCategory.objects.all()
    }
    #context['products'] = json.load((open(file_path, encoding='utf-8')))
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    # Контроллер вывода информации о продукте
    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
