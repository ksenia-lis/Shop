from django.shortcuts import render
from shop.models import product
from shop.models import comment
from django.http import Http404
from django.template import Context, loader
from .models import producer
from .models import category
from .models import order
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

def cart(request, username):
    # t = loader.get_template('shop/base.html')
    #return HttpResponse(t.render())
    return HttpResponse("it's your cart")


def home(request):
    t = loader.get_template('shop/home.html')
    categories_list =  category.objects.all()
    c = Context({
        'categories_list': categories_list,
    })
    return HttpResponse(t.render(c))
    #return HttpResponse("You're at home")

def catalog(request):
    t = loader.get_template('shop/catalog.html')
    categories_list =  category.objects.all()
    c = Context({
        'categories_list': categories_list,
    })
    return HttpResponse(t.render(c))
    #return HttpResponse("You're in catalog")

def Product(request, product_id):
    #t = loader.get_template('shop/product.html')
    comments_list = comment.objects.all()
   # c = Context({
    #    'comments_list': comments_list,
    #})
    p = get_object_or_404(product, pk=product_id)
    #return HttpResponse(t.render(c, p))
   #
    return render(request, 'shop/product.html', context ={"product" : p,
                                                          "comments_list": comments_list})


def OneCategory(request, category_id):
    p = get_object_or_404(category, pk=category_id)
    products = product.objects.filter(category=category_id)[:]
    t = loader.get_template('shop/category.html')
    c = Context({
        'products_list': products,
    })
    return HttpResponse(t.render(c))


def MyOrders(request, user_id):
    return HttpResponse("You're looking at your orders")


def Authorisation(request):
    return render(request, 'shop/sign-in.html')


def Order(request, order_id):
    return HttpResponse("You're looking at this order")


