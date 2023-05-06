from django.urls import path
from . import views

urlpatterns = [
    path('', views.BrowseHomePage.as_view(), name='home'),
    path('game/<slug:game_slug>', views.product_detail, name='games'),
    path('catalog/', views.Catalog.as_view(), name='catalog'),
    path('catalog/<slug>', views.Catalog.as_view(), name='catalog_view'),
    path('catalog/search/', views.Catalog.as_view(), name='catalog_search'),

]

# изменить путь к каталогу catalog/<slug:category_Slug> на основании выбранной категории