# Generated by Django 4.0.4 on 2022-06-12 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting_uom', '0003_groupuom_groupuomdefinition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uom',
            name='uom_code',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]
