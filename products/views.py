from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Product
from django.core.paginator import Paginator


class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        paginator = Paginator(products, 10)  # Разбиваем список продуктов на страницы по 10 элементов

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'title': 'Список продуктов',
            'products': products
        }
        return render(request, "products/index.html", context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-details.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


class ProductListView(ListView):
    model = Product
    template_name = 'products/product-list.html'
    context_object_name = 'product_list'
