# Generated by Django 4.0.2 on 2022-02-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_alter_searchterm_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchterm',
            name='conversion_value',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]