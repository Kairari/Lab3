# Generated by Django 2.0.3 on 2018-04-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='carts',
            field=models.ManyToManyField(blank=True, to='commerce.Cart'),
        ),
    ]
