from django.urls import path
from . import views


app_name = 'item'
urlpatterns = [
    path('<int:pk>/', views.item_list, name='detail'),
]