# Generated by Django 3.1.1 on 2020-10-11 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20201011_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_images',
        ),
    ]