from django.db import models
# Create your models here.
from django.utils.text import slugify


class Delivery_Person(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Delivery_Person, self).save(*args, **kwargs)
