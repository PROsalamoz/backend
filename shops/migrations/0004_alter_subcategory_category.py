# Generated by Django 3.2 on 2021-04-28 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_alter_shop_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bigCategory', to='shops.category'),
        ),
    ]
