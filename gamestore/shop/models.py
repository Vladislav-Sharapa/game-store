from django.db import models
from django.core.validators import MinValueValidator 
from decimal import Decimal
from django.urls import reverse
from PIL import Image
# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,verbose_name="URL")
    description = models.TextField(blank=True)
    vertical_photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    horizontal_photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    price = models.DecimalField(decimal_places=2, max_digits=7, validators=[MinValueValidator(Decimal('1.00'))])
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('games', kwargs={'game_slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        vertical_img = Image.open(self.vertical_photo.path)
        horizontal_img = Image.open(self.horizontal_photo.path)

        if vertical_img.width != 400 or vertical_img.height != 500:
            size = (400, 500)
            vertical_img.thumbnail(size)
            vertical_img.save(self.vertical_photo.path)

        if horizontal_img.width != 450 or horizontal_img.height != 300:
            size = (450, 250)
            horizontal_img.thumbnail(size)
            horizontal_img.save(self.horizontal_photo.path)


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
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('category', kwargs={'category_slug': self.slug})

