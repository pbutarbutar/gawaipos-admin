# Generated by Django 4.0.4 on 2022-06-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microweb', '0005_aboutus_merchant_id_productlist_merchant_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlistimages',
            name='facebook_link',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='productlistimages',
            name='linked_link',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='productlistimages',
            name='twitter_link',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='productlistimages',
            name='youtube_link',
            field=models.CharField(default='', max_length=150),
        ),
    ]