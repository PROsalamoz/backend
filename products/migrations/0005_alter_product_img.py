# Generated by Django 3.2 on 2021-04-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210429_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='cloud.jpg', upload_to='images'),
        ),
    ]
