# Generated by Django 3.2.9 on 2021-11-19 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolioApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DentistProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clinic', models.CharField(max_length=100, null=True)),
                ('Address1', models.CharField(max_length=100, null=True)),
                ('Address2', models.CharField(max_length=100, null=True)),
                ('City', models.CharField(max_length=100, null=True)),
                ('Postcode', models.CharField(max_length=100, null=True)),
                ('Country', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
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
        migrations.CreateModel(
            name='ImageUploadAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image1', models.FileField(upload_to='')),
                ('Image2', models.FileField(upload_to='')),
                ('Image3', models.FileField(upload_to='')),
                ('Time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
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
        migrations.CreateModel(
            name='IncomeExpenseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeExpenseTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LabWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('PatientName', models.CharField(max_length=100)),
                ('PatientID', models.CharField(max_length=100, null=True)),
                ('Dentist', models.CharField(max_length=100)),
                ('Scheme', models.CharField(max_length=100)),
                ('Lab', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=50, null=True)),
                ('Quantity', models.CharField(max_length=50, null=True)),
                ('Note', models.CharField(max_length=50, null=True)),
                ('Stage', models.CharField(max_length=40, null=True)),
                ('Status', models.CharField(max_length=40, null=True)),
                ('DateArriving', models.CharField(max_length=20, null=True)),
                ('Arrived', models.CharField(max_length=40, null=True)),
                ('Fee', models.FloatField()),
                ('PaidDate', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('user', models.CharField(max_length=40, null=True)),
                ('Item', models.CharField(max_length=100, null=True)),
                ('Category', models.CharField(max_length=100)),
                ('OrderBy', models.CharField(max_length=100)),
                ('Supplier', models.CharField(max_length=100)),
                ('Quantity', models.CharField(max_length=50, null=True)),
                ('Fee', models.FloatField(null=True)),
                ('NewDate', models.DateField(null=True)),
                ('Arrived', models.CharField(max_length=20, null=True)),
                ('Returned', models.CharField(max_length=20, null=True)),
                ('Note', models.CharField(max_length=200, null=True)),
                ('Status', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prescriber', models.CharField(max_length=100)),
                ('Clinic', models.CharField(max_length=300)),
                ('Email', models.CharField(max_length=300)),
                ('Telephone', models.CharField(max_length=300)),
                ('PatientName', models.CharField(max_length=100)),
                ('Sex', models.CharField(max_length=100)),
                ('TreatmentInPast', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('Address1', models.CharField(max_length=100)),
                ('Address2', models.CharField(max_length=100)),
                ('OralScan', models.CharField(max_length=100)),
                ('Impression', models.CharField(max_length=100)),
                ('UpperJaw', models.FileField(upload_to='')),
                ('LowerJaw', models.FileField(upload_to='')),
                ('Photo1', models.ImageField(upload_to='')),
                ('Photo2', models.ImageField(upload_to='')),
                ('Photo3', models.ImageField(upload_to='')),
                ('Photo4', models.ImageField(upload_to='')),
                ('Treatment', models.CharField(max_length=50)),
                ('TreatmentRequired', models.CharField(max_length=50)),
                ('Aligners', models.CharField(max_length=50)),
                ('TreatmentLimit', models.CharField(max_length=50)),
                ('Overbite', models.CharField(max_length=50)),
                ('Overjet', models.CharField(max_length=50)),
                ('Expension', models.CharField(max_length=50)),
                ('IPR', models.CharField(max_length=50)),
                ('Procline', models.CharField(max_length=50)),
                ('Distalize', models.CharField(max_length=50)),
                ('UpperMidline', models.CharField(max_length=50)),
                ('LoverMidline', models.CharField(max_length=50)),
                ('ArchForm', models.CharField(max_length=50)),
                ('PCrossbite', models.CharField(max_length=50)),
                ('Hint1', models.CharField(max_length=50)),
                ('Hint2', models.CharField(max_length=50)),
                ('Hint3', models.CharField(max_length=50)),
                ('DentistNote', models.TextField(default='Not Added')),
                ('AdminNote', models.TextField(default='Not Added')),
                ('Status', models.CharField(choices=[('Accept', 'Accept'), ('Review', 'Review'), ('Decline', 'Decline'), ('On-Hold', 'On-Hold')], default='Pending', max_length=20)),
                ('InternalStatus', models.CharField(default='On', max_length=30)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientProposedTreatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProposedTreatment', models.FileField(null=True, upload_to='')),
                ('ThreeDViewProposed', models.FileField(null=True, upload_to='')),
                ('Invoice', models.FileField(null=True, upload_to='')),
                ('Time', models.DateTimeField(auto_now_add=True, null=True)),
                ('Patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('User', models.CharField(max_length=50)),
                ('PatientName', models.CharField(max_length=50)),
                ('Dentist', models.CharField(max_length=50)),
                ('Scheme', models.CharField(max_length=50)),
                ('PaymentMethod', models.CharField(max_length=50)),
                ('Amount', models.FloatField()),
                ('Status', models.CharField(default='Pending', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DentistName', models.CharField(max_length=50, null=True)),
                ('PatientName', models.CharField(max_length=50)),
                ('PatientPhone', models.CharField(max_length=20)),
                ('PatientEmail', models.CharField(max_length=40)),
                ('ReferralReason', models.CharField(choices=[('Consultation', 'Consultation'), ('Implant', 'Implant'), ('Orthodontics', 'Orthodontics'), ('Root Canal Treatment', 'Root Canal Treatment'), ('Implant', 'Crown and Veneers')], default='Consultation', max_length=60, null=True)),
                ('Status', models.CharField(choices=[('Inprogress', 'Inprogress'), ('Accepted', 'Accepted'), ('TC', 'TC'), ('Declined', 'Declined')], default='In Progress', max_length=40, null=True)),
                ('BookedOn', models.CharField(max_length=40, null=True)),
                ('TreatmentPlan', models.CharField(max_length=80, null=True)),
                ('Note', models.CharField(max_length=150, null=True)),
                ('Stage', models.CharField(max_length=150, null=True)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Dentist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentRequestFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='Question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='Post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='querie',
            name='user',
        ),
        migrations.DeleteModel(
            name='Website',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Querie',
        ),
        migrations.AddField(
            model_name='imageuploadadmin',
            name='Patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.patient'),
        ),
        migrations.AddField(
            model_name='imageuploadadmin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
