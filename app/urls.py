from django.urls import path, include
from .views import index, product, categories, listing

urlpatterns = [

    path('', index),
    path('product/', product),
    path('category/', categories),
    path('listing/', listing),
]
