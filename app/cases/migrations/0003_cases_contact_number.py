# Generated by Django 4.0.1 on 2022-03-15 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_cases_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='contact_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='contact_number'),
        ),
    ]
