# Generated by Django 4.0.4 on 2022-06-12 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0001_initial'),
        ('inventory', '0002_stockonhand_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockonhand',
            name='merchant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inv_merchant_id', to='merchants.merchant'),
        ),
    ]
