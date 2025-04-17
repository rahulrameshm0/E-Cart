from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product_details/', views.product_details,name='product_details'),
]
