# Generated by Django 4.0.4 on 2022-06-17 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employies', '0002_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='departement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_departement_id', to='employies.department'),
        ),
    ]