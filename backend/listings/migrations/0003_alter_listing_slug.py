# Generated by Django 4.0.3 on 2022-06-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]