from django.urls import path
from . import views


app_name = 'category'
urlpatterns = [
    path('<str:name>/', views.item_in_category, name='category'),
]