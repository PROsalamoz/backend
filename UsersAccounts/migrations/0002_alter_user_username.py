# Generated by Django 3.2 on 2021-04-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersAccounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]