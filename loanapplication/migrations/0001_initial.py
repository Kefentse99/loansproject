# Generated by Django 3.2.6 on 2021-08-31 19:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('customerName', models.CharField(max_length=200)),
                ('creditrating', models.IntegerField(max_length=3)),
                ('occupation', models.CharField(max_length=100)),
                ('netIncome', models.IntegerField()),
            ],
        ),
    ]