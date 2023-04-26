from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Game
from .Cart import Cart

# Create your views here.

@require_POST
def cart_add(request, game_slug):
    cart = Cart(request)
    game = get_object_or_404(Game, slug=game_slug)
    cart.add(game=game)

    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})