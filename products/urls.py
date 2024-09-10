from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.list_products, name='product_list'),
    path('api/products/create/', views.create_product, name='product_create'),
    path('', views.index, name='index'),
]
