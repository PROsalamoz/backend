# Generated by Django 3.2 on 2021-04-15 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=100)),
                ('description', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='images')),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('product', models.ManyToManyField(to='products.Product')),
            ],
        ),
    ]