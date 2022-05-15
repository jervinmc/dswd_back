# Generated by Django 4.0.1 on 2022-03-28 05:49

from django.db import migrations, models
import ps.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=255, null=True, verbose_name='PS')),
                ('lastname', models.CharField(blank=True, max_length=255, null=True, verbose_name='package')),
                ('middlename', models.CharField(blank=True, max_length=255, null=True, verbose_name='descriptions')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='status')),
                ('remarks', models.CharField(blank=True, max_length=255, null=True, verbose_name='remarks')),
                ('user_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='user_id')),
                ('image', models.ImageField(default='uploads/PS.png', upload_to=ps.models.nameFile, verbose_name='image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
