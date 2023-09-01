from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogposts, name='blogposts'),
    path('products/', views.product_list_view, name='product'),

 ]