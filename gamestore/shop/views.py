from django.shortcuts import render, get_object_or_404
from .models import Game, Category
from django.views import generic
from django.core.paginator import Paginator
import random

def main(request):
    return render(request, 'shop/home.html')


def product_detail(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    
    context = {
        'game' : game,
    }

    return render(request, 'shop/product.html', context=context)


class Catalog(generic.ListView):
    paginate_by = 6
    context_object_name = 'games'
    template_name = 'shop/catalog.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if self.kwargs.get('slug'):
            games = Category.objects.get(slug=self.kwargs['slug']).game_set.all() # receive all games of the same category
        elif query:
            games = Game.objects.filter(title__icontains=query)
        else:
            games = Game.objects.all()
        return games

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.kwargs.get('slug'):
            context['current_category'] = Category.objects.get(slug=self.kwargs['slug']).name
        else:
            context['current_category'] = 'All category'
        return context


class BrowseHomePage(generic.ListView):
    template_name = 'shop/home.html'
    context_object_name = 'games'
    
    def get_queryset(self):
        games = Game.objects.all()
        possible_id = random.sample(list(games.values_list('id', flat=True)), 8)

        return games.filter(pk__in=possible_id)