from django.db import models

from login.models import User


class ProductsCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    content = models.TextField(verbose_name='Описание', blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    slug = models.SlugField()
    category = models.ForeignKey(ProductsCategory, on_delete=models.PROTECT, related_name='category')

    def __str__(self):
        return self.title


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def sum(self):
        return self.product.price * self.quantity
