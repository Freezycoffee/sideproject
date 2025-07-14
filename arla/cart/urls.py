from django.urls import path
from . import views


app_name = 'cart'
urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/', views.addToCart, name='add'),
    path('delete/', views.deleteFromCart, name='delete'),
    path('update/', views.updateCart, name='update'),
]