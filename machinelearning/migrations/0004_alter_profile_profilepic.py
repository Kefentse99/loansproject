# Generated by Django 3.2.6 on 2021-10-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machinelearning', '0003_profile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilepic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
