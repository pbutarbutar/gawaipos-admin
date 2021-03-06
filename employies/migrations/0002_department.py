# Generated by Django 4.0.4 on 2022-06-17 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0002_merchant_merchant_address_merchant_merchant_email_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement_code', models.CharField(max_length=50, unique=True)),
                ('departement_name', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_dept', to=settings.AUTH_USER_MODEL)),
                ('merchant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_merchant_id', to='merchants.merchant')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_dept', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
