# Generated by Django 3.2.13 on 2022-04-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0026_rename_lowerarchbox_patient_lowerarchmaterial_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lowerarchbox',
            name='stage16',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lowerarchbox',
            name='stage17',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lowerarchbox',
            name='stage18',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lowerarchbox',
            name='stage19',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lowerarchbox',
            name='stage20',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='upperarchbox',
            name='stage16',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='upperarchbox',
            name='stage17',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='upperarchbox',
            name='stage18',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='upperarchbox',
            name='stage19',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='upperarchbox',
            name='stage20',
            field=models.BooleanField(default=False),
        ),
    ]
