# Generated by Django 4.0.1 on 2022-03-14 06:06

import cases.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.CharField(blank=True, max_length=255, null=True, verbose_name='price')),
                ('firstname', models.CharField(blank=True, max_length=255, null=True, verbose_name='firstname')),
                ('lastname', models.CharField(blank=True, max_length=255, null=True, verbose_name='lastname')),
                ('middlename', models.CharField(blank=True, max_length=255, null=True, verbose_name='middlename')),
                ('category', models.CharField(blank=True, max_length=255, null=True, verbose_name='category')),
                ('image', models.ImageField(default='uploads/Cases.png', upload_to=cases.models.nameFile, verbose_name='image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
