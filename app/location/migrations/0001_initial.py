# Generated by Django 4.0.1 on 2022-03-14 06:06

from django.db import migrations, models
import location.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=255, null=True, verbose_name='price')),
                ('package', models.CharField(blank=True, max_length=255, null=True, verbose_name='package')),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True, verbose_name='descriptions')),
                ('image', models.ImageField(default='uploads/Events.png', upload_to=location.models.nameFile, verbose_name='image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
