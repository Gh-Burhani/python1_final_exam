from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import BlogPost
from .models import Product


def blogposts(reqquest):
    post = BlogPost.objects.all().values()
    template = loader.get_template('myfirst.html')
    context= {
        'Post': post
    }
    return HttpResponse(template.render(context, reqquest))



def product_list_view(request):

  products = Product.objects.all().values()
  template = loader.get_template('product_list_view.html')
  context = {
    'products': products
  }
  return HttpResponse(template.render(context, request))

