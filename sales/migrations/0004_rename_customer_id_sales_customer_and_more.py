# Generated by Django 4.0.4 on 2022-06-14 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting_uom', '0007_rename_merchant_id_groupuom_merchant_and_more'),
        ('sales', '0003_sales_merchant_id_salesdetails_merchant_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='sales',
            old_name='merchant_id',
            new_name='merchant',
        ),
        migrations.RenameField(
            model_name='salesdetails',
            old_name='item_id',
            new_name='catalog',
        ),
        migrations.RenameField(
            model_name='salesdetails',
            old_name='merchant_id',
            new_name='merchant',
        ),
        migrations.RenameField(
            model_name='salesdetails',
            old_name='sales_id',
            new_name='sales',
        ),
        migrations.RenameField(
            model_name='salesdetails',
            old_name='warehouse_id',
            new_name='warehouse',
        ),
        migrations.AddField(
            model_name='salesdetails',
            name='qty',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='salesdetails',
            name='uom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uom_sales_items', to='setting_uom.uom'),
        ),
    ]
