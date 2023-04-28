from decimal import Decimal
from gamestore import settings
from shop.models import Game


class Cart(object):
    def __init__(self, request):
        """Initializing Cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, game: Game) -> None:
        """Add game to the cart"""
        game_id = str(game.id)
        if game_id not in self.cart:
            self.cart[game_id] = {'price':str(game.price)}
        
        self.save()


    def remove(self, game: Game) -> None:
        """Remove game from cart"""
        game_id = str(game.id)
        if game_id in self.cart:
            del self.cart[game_id]
            self.save()

    def save(self) -> None:
        """Save modified session"""
        self.session.modified = True

    def __iter__(self):
        """Iteration game in the cart"""
        game_ids = self.cart.keys()
        games = Game.objects.filter(id__in=game_ids)

        cart = self.cart.copy()

        for game in games:
            cart[str(game.id)]['game'] = game
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            yield item

    def get_total_price(self) -> Decimal:
        '''Get total price of all item in cart'''
        return sum(item['price'] for item in self.cart.values())
        
    def clear(self) -> None:
        """Clear cart"""
        del self.session[settings.CART_SESSION_ID]

        self.save()



