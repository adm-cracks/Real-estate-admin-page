# Generated by Django 4.2.7 on 2023-12-07 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_property_rent_cost_remove_property_unit_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='units',
            name='pro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pr', to='home.property'),
        ),
    ]