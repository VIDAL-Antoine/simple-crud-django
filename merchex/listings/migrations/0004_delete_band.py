# Generated by Django 4.2.3 on 2023-07-07 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Band',
        ),
    ]