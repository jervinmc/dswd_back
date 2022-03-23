# Generated by Django 4.0.1 on 2022-03-14 06:16

from django.db import migrations, models
import donate.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=255, null=True, verbose_name='donate')),
                ('lastname', models.CharField(blank=True, max_length=255, null=True, verbose_name='package')),
                ('middlename', models.CharField(blank=True, max_length=255, null=True, verbose_name='descriptions')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='status')),
                ('image', models.ImageField(default='uploads/Donate.png', upload_to=donate.models.nameFile, verbose_name='image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]