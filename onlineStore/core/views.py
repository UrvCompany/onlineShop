from django.shortcuts import render, get_object_or_404
from  .models import Product, Category


def popular_list(request):
    """

    :param request:
    :return:
    """

    products = Product.objects.filter(available=True)[:3]
    return render(request,
                  'core/index/index.html',
                  {'products': products})


def product_detail(request, slug):
    """

    :param request:
    :param slug:
    :return:
    """

    product = get_object_or_404(Product,
                                slug=slug,
                                available=True)

    return render(request,
                  'core/product/detail.html',
                  {'product': product})


