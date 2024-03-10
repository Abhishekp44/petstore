from django.urls import path
from petstoreapp import views

urlpatterns = [
    path('home',views.home),
    #path('search',views.search),
    path('catfilter/<cv>',views.catfilter),
    path('pricefilter',views.pricefilter),
]
