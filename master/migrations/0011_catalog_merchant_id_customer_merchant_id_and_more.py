# Generated by Django 4.0.4 on 2022-06-12 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0001_initial'),
        ('master', '0010_customer_created_at_customer_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='merchant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='catalog_merchant_id', to='merchants.merchant'),
        ),
        migrations.AddField(
            model_name='customer',
            name='merchant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_merchant_id', to='merchants.merchant'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='merchant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_merchant_id', to='merchants.merchant'),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='merchant_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wh_merchant_id', to='merchants.merchant'),
        ),
    ]
