# Generated by Django 4.0.1 on 2022-04-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0019_alter_patientproposedtreatment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Progress',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
