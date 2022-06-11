# Generated by Django 4.0.4 on 2022-06-11 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_vehicle_brand_fk', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_vehicle_brand_fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_vehicle_fk', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_vehicle_fk', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='VehicleOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=50)),
                ('owner_hp', models.CharField(max_length=50)),
                ('owner_email', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_vehicle_owner_fk', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_vehicle_owner_fk', to=settings.AUTH_USER_MODEL)),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_id_owner_fk', to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_vehicle_category_fk', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_vehicle_category_fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleBrandOfType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_type', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehiclebrand')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_vehicle_brand_type_fk', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_vehicle_brand_type_fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='brand_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_brand_id_fk', to='vehicles.vehiclebrand'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='brand_type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_type_fk', to='vehicles.vehiclebrand'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_category_id_fk', to='vehicles.vehiclecategory'),
        ),
    ]
