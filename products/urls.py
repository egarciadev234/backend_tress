from django.contrib import admin
from django.conf.urls import url, include
from .views import *
urlpatterns = [
    url(r'^api/v1/brands/$', ListBrands.as_view(), name='list-brands'),
    url(r'^api/v1/categories/$', ListCategories.as_view(), name='list-categories'),

    url(r'^api/v1/products/$', ListProducts.as_view(), name='list-products'),
    url(r'^api/v1/product/(?P<uuid>[\w\-]+)/$', DetailProduct.as_view(), name='detail-product'),

    url(r'^api/v1/products/images/$', ImagesProducts.as_view(), name='list-products-images'),
    url(r'^api/v1/product/images/(?P<product>[\w\-]+)/$', DetailsImagesProduct.as_view(), name='list-product-images'),
]