# Generated by Django 4.0.1 on 2022-03-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiaries', '0003_beneficiaries_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiaries',
            name='firstname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='firstname'),
        ),
    ]