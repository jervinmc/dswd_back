# Generated by Django 4.0.1 on 2022-04-26 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sap', '0005_sap_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='sap',
            name='date_start',
            field=models.DateField(blank=True, null=True, verbose_name='date_start'),
        ),
    ]
