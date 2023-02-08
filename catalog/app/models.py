from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")

    def __str__(self):
        return self.email


class Category(models.Model):
    """Category"""
    title = models.CharField(max_length=255, verbose_name="Категория")

    def __str__(self):
        return self.title


class Product(models.Model):
    """Product"""
    PACKAGE_CHOICES = (
        ("B", "Без упаковки"),
        ("P", "Подарочная"),
        ("W", "С бокалом"),
    )

    title = models.CharField(max_length=255, verbose_name="Название товара")
    title_rus = models.CharField(max_length=255,
                                 verbose_name="Название товара на русском")
    image = models.ImageField(upload_to='wines', verbose_name="Фото", null=True, blank=True)
    # categories = models.ForeignKey(Category, on_delete=models.CASCADE,
    #                                verbose_name="Категория",
    #                                null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                verbose_name="Цена")
    country = models.CharField(max_length=50, verbose_name="Страна")
    region_manufacture = models.CharField(max_length=50,
                                          verbose_name="Регион производства")
    fortress = models.DecimalField(max_digits=4, decimal_places=2,
                                   verbose_name="Крепость")
    manufacturer = models.CharField(max_length=120,
                                    verbose_name="Производитель")
    volume = models.DecimalField(max_digits=4, decimal_places=3,
                                 verbose_name="Объем")
    packaging = models.CharField(max_length=1, choices=PACKAGE_CHOICES)
    brand = models.CharField(max_length=100, verbose_name="Бренд")
    description = models.TextField(verbose_name="Описание")
    stock = models.BooleanField(default=False, verbose_name="В наличии")
    created_date = models.DateField(auto_now_add=True,
                                    verbose_name="Дата создание")
    updated_date = models.DateField(auto_now=True,
                                    verbose_name="Дата корректировки")

    class Meta:
        abstract = True

    def __str__(self):
        return self.title_rus


class Wine(Product):
    """Wine"""

    COLOR_TYPE = (
        ("W", "Белое"),
        ("R", "Красное"),
        ("P", "Розовое"),
        ("G", "Зеленое"),
    )

    SUGAR_AMOUNT = (
        ("S", "Сладкое"),
        ("SS", "Полусладкое"),
        ("SD", "Полусухое"),
        ("D", "Сухое"),
    )

    color = models.CharField(max_length=1, choices=COLOR_TYPE, default="W")
    sugar = models.CharField(max_length=2, choices=SUGAR_AMOUNT, default="S")
    grape_variety = models.CharField(
        max_length=50,
        verbose_name="Сорт винограда"
    )
    recommended_temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Температура подачи"
    )

    def __str__(self):
        return self.title_rus
