from django.db import models
from django.core.validators import MinValueValidator 
from decimal import Decimal
from django.urls import reverse

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,verbose_name="URL")
    description = models.TextField(blank=True)
    photo =models.ImageField(upload_to="photos/%Y/%m/%d/")
    price = models.DecimalField(decimal_places=2, max_digits=7, validators=[MinValueValidator(Decimal('1.00'))])
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('games', kwargs={'id': self.id})
    
    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
        # порядок сортировки
        ordering = ['title']


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        # порядок сортировки
        ordering = ['name']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'id': self.id})

