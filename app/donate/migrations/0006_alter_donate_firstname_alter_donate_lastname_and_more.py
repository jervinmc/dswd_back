# Generated by Django 4.0.1 on 2022-05-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0005_donate_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='firstname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='firstname'),
        ),
        migrations.AlterField(
            model_name='donate',
            name='lastname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='lastname'),
        ),
        migrations.AlterField(
            model_name='donate',
            name='middlename',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='middlename'),
        ),
    ]
