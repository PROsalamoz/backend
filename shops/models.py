from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Shop(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Shop, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class ShopCategory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_category")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="shop_category")


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
