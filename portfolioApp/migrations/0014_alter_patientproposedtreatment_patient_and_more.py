# Generated by Django 4.0.1 on 2022-04-06 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolioApp', '0013_patient_action_patient_adminstatus_patient_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientproposedtreatment',
            name='Patient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.patient'),
        ),
        migrations.AlterField(
            model_name='patientproposedtreatment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='referral',
            name='ReferralReason',
            field=models.CharField(choices=[('Consultation', 'Consultation'), ('Implant', 'Implant'), ('Orthodontics', 'Orthodontics'), ('Root Canal', 'Root Canal'), ('Crown', 'Crown')], default='Consultation', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='referral',
            name='Status',
            field=models.CharField(choices=[('New', 'New'), ('Booked', 'Booked'), ('Declined', 'Declined'), ('TC', 'TC')], default='New', max_length=40, null=True),
        ),
    ]
