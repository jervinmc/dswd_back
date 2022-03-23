# Generated by Django 4.0.1 on 2022-03-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_cases_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='cases',
            name='age',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='age'),
        ),
        migrations.AddField(
            model_name='cases',
            name='attainment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='attainment'),
        ),
        migrations.AddField(
            model_name='cases',
            name='attended',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='attended'),
        ),
        migrations.AddField(
            model_name='cases',
            name='birthplace',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='birthplace'),
        ),
        migrations.AddField(
            model_name='cases',
            name='birthplace_father',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='birthplace_father'),
        ),
        migrations.AddField(
            model_name='cases',
            name='birthplace_mother',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='birthplace_mother'),
        ),
        migrations.AddField(
            model_name='cases',
            name='fathername',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='fathername'),
        ),
        migrations.AddField(
            model_name='cases',
            name='mothername',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='mothername'),
        ),
        migrations.AddField(
            model_name='cases',
            name='number_of_siblings',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='number_of_siblings'),
        ),
        migrations.AddField(
            model_name='cases',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='occupation'),
        ),
        migrations.AddField(
            model_name='cases',
            name='occupation_mother',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='occupation_mother'),
        ),
        migrations.AddField(
            model_name='cases',
            name='parentsaddress',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='parentsaddress'),
        ),
        migrations.AddField(
            model_name='cases',
            name='religion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='religion'),
        ),
        migrations.AddField(
            model_name='cases',
            name='sex',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='sex'),
        ),
    ]
