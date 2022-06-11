# Generated by Django 4.0.4 on 2022-06-11 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_vehiclebrand_alter_vehicle_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='brand_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_brand_id_fk', to='vehicles.vehiclebrand'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='brand_type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_type_fk', to='vehicles.vehiclebrand'),
        ),
    ]
