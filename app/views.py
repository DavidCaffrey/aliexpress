from django.shortcuts import render


def index(request):
    return render(request, 'page-index.html', {})


def product(request):
    return render(request,'page-detail-product.html', {})


def categories(request):
    return render(request, 'page-category.html', {})


def listing(request):
    return render(request, 'page-listing-large.html', {})
