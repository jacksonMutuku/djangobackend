# Generated by Django 4.0 on 2022-10-09 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('phoneNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtor.contacts')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realtor.contacts')),
            ],
        ),
        migrations.CreateModel(
            name='ForSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('coverPhoto', models.ImageField(blank='false', null='false', upload_to='uploads/images')),
                ('photos', models.ImageField(blank='false', null='false', upload_to='', verbose_name='uploads/photos')),
                ('purpose', models.CharField(max_length=50)),
                ('furnishingStatus', models.CharField(max_length=50)),
                ('housetype', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('rooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('price', models.IntegerField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realtor.propertyowner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ForRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('coverPhoto', models.ImageField(blank='false', null='false', upload_to='uploads/images')),
                ('photos', models.ImageField(blank='false', null='false', upload_to='', verbose_name='uploads/photos')),
                ('purpose', models.CharField(max_length=50)),
                ('furnishingStatus', models.CharField(max_length=50)),
                ('housetype', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('rooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('rentamount', models.IntegerField(blank=True)),
                ('rentFrequency', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realtor.propertyowner')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
