from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Watch, CartItem, Profile
from .forms import SignUpForm


def cart_count(request):
    """Shows the number of items in the cart on every page."""
    if request.user.is_authenticated:
        return {"cart_count": sum(i.quantity for i in CartItem.objects.filter(user=request.user))}
    return {"cart_count": 0}


def home(request):
    watches = Watch.objects.all()
    return render(request, "store/home.html", {"watches": watches})


def about(request):
    return render(request, "store/about.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data["email"]
            user.save()
            Profile.objects.create(user=user, phone=form.cleaned_data["phone"],
                                   address=form.cleaned_data["address"])
            login(request, user)
            messages.success(request, "Welcome! Your account was created.")
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "store/signup.html", {"form": form})


@login_required
def add_to_cart(request, watch_id):
    watch = get_object_or_404(Watch, id=watch_id)
    item, created = CartItem.objects.get_or_create(user=request.user, watch=watch)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f"{watch.name} added to your cart.")
    return redirect("home")


@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(i.subtotal() for i in items)
    return render(request, "store/cart.html", {"items": items, "total": total})


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect("cart")
