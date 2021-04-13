from django.db import models
from django.utils.text import slugify


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
        return self.nam

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)