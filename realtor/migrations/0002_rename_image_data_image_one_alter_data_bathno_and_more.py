# Generated by Django 4.0 on 2022-08-13 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='image',
            new_name='image_one',
        ),
        migrations.AlterField(
            model_name='data',
            name='bathno',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='data',
            name='price',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='rentamount',
            field=models.IntegerField(blank=True),
        ),
    ]
