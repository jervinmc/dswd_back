# Generated by Django 4.0.1 on 2022-04-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0003_donate_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='category'),
        ),
    ]
