# Generated by Django 3.2.9 on 2021-12-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0005_income_repeatstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='RepeatStatus',
            field=models.CharField(default='On', max_length=20, null=True),
        ),
    ]
