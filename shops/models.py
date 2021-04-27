from django.db import models
from django.utils.text import slugify



def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str


class Shop(models.Model):
    ShopId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    img = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='shops_in_category')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            if not self.slug:
                self.slug = arabic_slugify(self.name)
        super(Shop, self).save(*args, **kwargs)


class Category(models.Model):
    CategoryId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            if not self.slug:
                self.slug = arabic_slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class ShopCategory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_category")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="shop_category")


class SubCategory(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name="category")
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)
