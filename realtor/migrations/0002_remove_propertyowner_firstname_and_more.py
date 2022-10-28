# Generated by Django 4.0 on 2022-10-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyowner',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='propertyowner',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='lastname',
        ),
        migrations.AddField(
            model_name='contacts',
            name='firstname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacts',
            name='lastname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
