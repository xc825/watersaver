# Generated by Django 4.2 on 2023-09-30 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0005_property_inhabitants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='inhabitants',
            new_name='persons',
        ),
    ]
