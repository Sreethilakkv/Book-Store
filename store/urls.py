from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),

]