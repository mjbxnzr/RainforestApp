# Generated by Django 3.2.9 on 2021-11-25 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211125_0923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Unit_available',
            new_name='unit_available',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Unit_cost',
            new_name='unit_cost',
        ),
    ]
