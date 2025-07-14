from django.shortcuts import render
from item.models import Item, Category

# Create your views here.
def item_in_category(request, name: str):

    category = Category.objects.get(name=name)

    products = Item.objects.filter(category=category)

    return render(request, 'category/category.html', {'products': products, 'category': category})