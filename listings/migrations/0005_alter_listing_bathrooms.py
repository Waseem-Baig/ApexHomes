# Generated by Django 4.2.6 on 2023-11-03 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_bathrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=0, max_digits=1),
        ),
    ]