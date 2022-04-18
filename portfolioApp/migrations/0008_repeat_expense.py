# Generated by Django 4.0.1 on 2022-01-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0007_alter_labwork_tc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repeat_Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Title', models.CharField(max_length=50)),
                ('Category', models.CharField(max_length=50)),
                ('Account', models.CharField(max_length=50)),
                ('Amount', models.FloatField()),
                ('Status', models.CharField(max_length=20, null=True)),
                ('Note', models.TextField()),
                ('Repeat', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
