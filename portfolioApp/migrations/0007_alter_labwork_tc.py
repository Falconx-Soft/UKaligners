# Generated by Django 3.2.9 on 2021-12-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0006_alter_income_repeatstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labwork',
            name='TC',
            field=models.CharField(default=' ', max_length=20, null=True),
        ),
    ]
