from django.contrib import admin
from .models import Category, Game

# Register your models here.


class GameAdmin(admin.ModelAdmin):
    # отображаемые поля в админке
    list_display = ('id', 'title','price')
    list_display_links = ('id', 'title')
    # поиск по полям
    search_fields = ('title', 'price')
    prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    # отображаемые поля в админке
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    # поиск по полям
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Game, GameAdmin)
admin.site.register(Category)
