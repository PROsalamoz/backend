# Generated by Django 3.2 on 2021-04-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='cloud.jpg', null=True, upload_to='images'),
        ),
    ]