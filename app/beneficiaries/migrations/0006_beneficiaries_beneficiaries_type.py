# Generated by Django 4.0.1 on 2022-04-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiaries', '0005_beneficiaries_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiaries',
            name='beneficiaries_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='beneficiaries_type'),
        ),
    ]
