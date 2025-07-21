from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Max
from django.contrib.auth.models import User


from item.models import Item, Category
from .forms import SignupForm, updateProfileForm

def index(request):
    items = Item.objects.all()[:6]
    category = Category.objects.all()

    context = {
        'items': items,
        'categories': category,
    }
    return render(request, 'core/index.html', context=context)

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

def LogoutView(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('core:index')

def browse(request):
    items = Item.objects.all()
    max_price = Item.objects.aggregate(max_price=Max('price', default=0))
    category = Category.objects.all()
    context = {
        'items': items,
        'categories': category,
        'max_price': max_price['max_price'],
    }
    return render(request, 'core/browse.html', context=context)


def profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        # profile_form = updateProfileForm(request.POST or None, instance=request.user)
        context = {
            'user': user,
            # 'profile_form': profile_form
        }
    return render(request, 'core/profile.html',context=context)


def settings(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        profile_form = updateProfileForm(request.POST or None, instance=request.user)
        context = {
            'user': user,
            'profile_form': profile_form
        }

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
        
    return render(request, 'core/settings.html',context=context)




