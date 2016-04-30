from shop.models import User

from shop.models import ManufacturerCountry
from shop.models import comment
from shop.models import producer
from shop.models import product
from shop.models import category
from shop.models import order
from django.core.files import File
from datetime import datetime
import random


def g_username():
    s = ""
    for i in range(random.randint(6, 18)):
        s += random.choice("qwertyuiopasdfghjklzcvbxnm1234567890_-QWERTYUIOPASDFGHJKLZXCVBNM")
    return s


def g_email():
    s = ""
    for i in range(random.randint(13, 20)):
        s += random.choice("qwertyuiopasdfghjklzcvbxnm1234567890")
    s += random.choice(["@gmail.com", "@mail.ru", "@yandex.ru", "@yahoo.com"])
    return s

def g_password():
    s = ""
    for i in range(random.randint(20, 30)):
        s += random.choice("qwertyuiopasdfghjklzcvbxnm1234567890 QWERTYUIOPASDFGHJKLZXCVBNM_-")
    return s


def g_name():
    f = open('Random/names.txt')
    names = f.readlines()
    name = random.choice(names).strip()
    f.close()
    return name


def g_user():
    return User(username = g_username(), first_name = g_name(), last_name = g_surname(), email = g_email(), password = g_password())

def g_surname():
    f = open('Random/surnames.txt')
    surnames = f.readlines()
    surname = random.choice(surnames).strip()
    f.close()
    return surname


def g_country():
    f = open('Random/countries.txt')
    countries = f.readlines()
    f.close()
    return ManufacturerCountry(name = random.choice(countries).strip())

def g_category(i):
    f = open('Random/marks.txt')
    categories = f.readlines()
    name = categories[i]
    f.close()
    return category(name = name.strip())


def g_price():
    price = random.randint(1, 2000)
    return price

def get_object(variable):
    objects = variable.objects.all()[:]
    return random.choice(objects)


def g_product(amount_of_countries):
    f = open('Random/cars.txt')
    products = f.readlines()
    f.close()
    price = g_price()
    manufacturerCountry = ManufacturerCountry.objects.get(pk=random.randint(1, amount_of_countries))
    return product(name = random.choice(products).strip(), price = price, manufacturerCountry = manufacturerCountry)


def get_user():
    users = User.objects.all()[:]
    return random.choice(users)


def get_product():
    users = User.objects.all()[:]
    return random.choice(users)


def g_order(amount_of_users):
    user = User.objects.get(pk=random.randint(1, amount_of_users))
    return order(user = user)

def g_products(n):
    products = []
    amount_of_countries = ManufacturerCountry.objects.all().count()
    for i in range(n):
        products.append(g_product(amount_of_countries))
    product.objects.bulk_create(products)

def g_countries(n = 10):
    countries = []
    for i in range(n):
        countries.append(g_country())
    ManufacturerCountry.objects.bulk_create(countries)


def g_comment():
    f = open('Random/comments.txt')
    comments = f.readlines()
    f.close()
    return comment(text=random.choice(comments).strip())


def g_comments(n=50):
    comments = []
    for i in range(n):
        comments.append(g_comment())
    comment.objects.bulk_create(comments)


def g_categories(n = 10):
    objects = []
    for i in range(n):
        objects.append(g_category(i))
    category.objects.bulk_create(objects)


def g_users(n=10):
    users = []
    for i in range(n):
        users.append(g_user())
    User.objects.bulk_create(users)

def g_orders(n=10):
    orders = []
    amount_of_users = User.objects.all().count()
    for i in range(n):
        orders.append(g_order(amount_of_users))
    order.objects.bulk_create(orders)

def add_products_to_orders(n=10):
    i = 1
    amount_of_products = product.objects.all().count()
    while i < n+1:
        orderr = order.objects.get(id= i)
        j  = 1
        while j < random.randint(2, amount_of_products):
            j = j+1
            orderr.products.add(product.objects.get(pk=random.randint(1, amount_of_products)))
        i = i+1


def gen_like():
    post = get_random_post()
    usr = get_random_user()
    ThroughModel = Post.like_users.through
    return ThroughModel(post_id=post.id, user_id=usr.id)



def add_products_to_categories(n=134):
    i = 1
    amount_of_products = product.objects.all().count()
    ThroughModel = category.products.through
    while i < n+1:
        prdcts = []
        categoryy = category.objects.get(id= i)
        s=categoryy.name
        print (s)
        j  = 1
        while j <  amount_of_products:
            this_product = product.objects.get(id=j)
            #ThroughModel.category_id=i
            string = this_product.name
            if (string.find(s) > -1):
                #print string
                prdcts.append(this_product)
            j = j+1
        categoryy.products.through.objects.bulk_create(prdcts)
        i = i+1


def generate(n=3):
    g_comments(n=100)
    #g_users(n=n)
    ##g_countries(n=n)
    #g_producers(n=n)
    #g_categories(n=134)
    #g_orders(n=n)
    #g_products(n=n)
    #add_products_to_orders(n=n)
    #add_products_to_categories(n=134)

generate(n=500)
