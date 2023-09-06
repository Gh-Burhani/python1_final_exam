from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import BlogPost
from .models import Product


def blogposts(request):
    post = BlogPost.objects.all().values()
    template = loader.get_template('myfirst.html')
    context= {
        'post': post
    }
    return HttpResponse(template.render(context, request))


def product_list_view(request):
    product = Product.objects.all().values()
    template = loader.get_template('product_list_view.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))

