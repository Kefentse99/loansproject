# Generated by Django 3.2.6 on 2021-08-31 20:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('loanapplication', '0002_alter_customer_creditrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branchID', models.AutoField(primary_key=True, serialize=False)),
                ('branchName', models.CharField(max_length=100)),
                ('swiftKey', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LoanAgent',
            fields=[
                ('employeeID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('employeeName', models.CharField(max_length=200)),
                ('branch', models.ManyToManyField(blank=True, to='loanapplication.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='LoanGiven',
            fields=[
                ('loanID', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True)),
                ('loantype', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.TextField()),
                ('interest', models.IntegerField()),
                ('loandate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loaninfo',
            fields=[
                ('loadID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('loanName', models.CharField(max_length=200)),
                ('loanType', models.CharField(choices=[('car', 'Car Loan'), ('Home', 'Home Loan'), ('School', 'Student Loan'), ('personal', 'Personal Loan')], max_length=200)),
                ('loanDuration', models.CharField(max_length=20)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loanapplication.branch')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loanapplication.customer')),
                ('loanAgent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loanapplication.loanagent')),
            ],
        ),
    ]
