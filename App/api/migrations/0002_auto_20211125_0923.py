# Generated by Django 3.2.9 on 2021-11-25 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Unit_cost', models.FloatField()),
                ('Price', models.FloatField()),
                ('Unit_available', models.IntegerField()),
            ],
            options={
                'db_table': 'PRODUCT',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.product'),
        ),
        migrations.DeleteModel(
            name='Species',
        ),
    ]
