# Generated by Django 4.0 on 2022-08-15 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0003_alter_data_image_one'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='image_one',
            new_name='coverPhoto',
        ),
    ]
