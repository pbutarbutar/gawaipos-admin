# Generated by Django 3.2.13 on 2022-05-22 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_alter_catalog_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
