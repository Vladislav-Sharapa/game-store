from django import template
from shop.models import Game, Category
import random

# регистрация собственных шаблонных тегов
register = template.Library()

@register.inclusion_tag('shop/list_related_games.html')
def get_related_games(game):
    games = Category.objects.get(id=game.category.id).game_set.all() # получим все игры той же категории

    possible_ids = list(games.values_list('id', flat=True))

    if game.id in possible_ids:
        possible_ids.remove(game.id)
    
    # если игр в соответствующей категории будет больше, чем четыре
    if len(possible_ids) >= 4:
        possible_ids = random.sample(possible_ids, k=4)
        random_games = games.filter(pk__in=possible_ids)
        return {'games': random_games}
    else:
        return None