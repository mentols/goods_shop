from django.contrib.auth.models import User
from django.core import validators
from django.db import models


# история заказов и корзина


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.category_name


class Address(models.Model):
    street = models.CharField(max_length=255, null=False)
    house = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.street} {self.house} '


class Warehouse(models.Model):
    address = models.ForeignKey(to=Address, on_delete=models.CASCADE)
    capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'Склад на {self.address}'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cash = models.DecimalField(validators=[validators.MinValueValidator(limit_value=0)], max_digits=7, decimal_places=2)


class Good(models.Model):
    class GenderChoices(models.IntegerChoices):
        Male = 1
        Female = 2

    class SizeChoices(models.IntegerChoices):
        S = 1
        M = 2
        L = 3
        XL = 4

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.CharField(max_length=2000)
    description_tittle = models.CharField(max_length=255)
    size = models.PositiveSmallIntegerField(choices=SizeChoices.choices, null=False, default=1)
    cover = models.ImageField(upload_to='img/%Y-%m-%d/', null=True)
    gender = models.PositiveSmallIntegerField(choices=GenderChoices.choices, null=False, default=1)
    sale = models.PositiveSmallIntegerField(null=False, validators=[validators.MaxValueValidator(limit_value=100),
                                                                    validators.MinValueValidator(limit_value=0)],
                                            default=0)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.goods_name


class Order(models.Model):
    is_deliver = models.BooleanField(default=False, null=False)
    delivery_address = models.ForeignKey(to=Address, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, null=False)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'Заказ на улицу {self.delivery_address}'


class Content(models.Model):
    good = models.ForeignKey(to=Good, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(null=False)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)


class Photo(models.Model):
    picture = models.ImageField(upload_to='img/%Y-%m-%d/', null=True)
    good = models.ForeignKey(to=Good, on_delete=models.CASCADE)
