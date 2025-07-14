from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from item.models import Item
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def cart(request):
    cart = Cart(request)
    products = cart.get_item()
    quantity = cart.get_qty()
    return render(request, 'cart/cart.html', {'products': products, 'quantity': quantity,})

@login_required
def addToCart(request):
    # Get the cart
    cart = Cart(request)
    # test a POST
    if request.POST.get('action') == 'post':
        # fetch the item_id
        item_id = int(request.POST.get('item_id'))
        quantity = int(request.POST.get('quantity'))
        # get the item from db
        item = get_object_or_404(Item, id=item_id)
        # add the item to the cart
        cart.add(item, quantity)

        # get quantity
        qty = cart.__len__()

        response = JsonResponse({'Product Name': item.name, 'Price': item.price, 'Quantity': qty, 'Total Items': quantity, 'price': item.price})
        # response
        messages.success(request, 'Item added to cart')
        return response
    

def deleteFromCart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('item_id'))
        cart.remove(item_id)
        response = JsonResponse({'status': 'Deleted',})
        messages.success(request, 'Item removed from cart')
        return response

def updateCart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # fetch the item_id
        item_id = int(request.POST.get('item_id'))
        quantity = int(request.POST.get('quantity'))
        # get the item from db
        item = get_object_or_404(Item, id=item_id)

        # get quantity
        qty = cart.__len__()


        cart.update(item, quantity)
        response = JsonResponse({'Product Name': item.name, 'Price': item.price, 'Quantity': qty, 'Total Items': quantity, 'price': item.price})
        return response

