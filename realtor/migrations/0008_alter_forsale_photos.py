# Generated by Django 4.0 on 2022-08-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0007_forsale_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forsale',
            name='photos',
            field=models.ImageField(blank='false', null='false', upload_to='', verbose_name='uploads/photos'),
        ),
    ]
