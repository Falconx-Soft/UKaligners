# Generated by Django 4.0.1 on 2022-03-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0012_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Action',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='AdminStatus',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Note',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='Stage',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
