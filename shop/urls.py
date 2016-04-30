
from django.conf.urls import url
from . import views
#urlpatterns = [
 #   url(r'^$', views.test, name='test'),
#]
urlpatterns = [
    url(r'^$', views.home),
    url(r'^catalog/$',views.catalog),
    url(r'^product/(?P<product_id>\d+)/$', views.Product),
    url(r'^catalog/category/(?P<category_id>\d+)/$', views.OneCategory),
    url(r'^catalog/category/product/(?P<product_id>\d+)/$', views.Product),
    url(r'^category/product/(?P<product_id>\d+)/$', views.Product),
    url(r'cart/$', views.cart),
    url(r'^authorisation/', views.Authorisation),
]