# Generated by Django 5.0.6 on 2024-06-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_billinginfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='fname',
            field=models.CharField(default='Unknown', max_length=20),
        ),
        migrations.AddField(
            model_name='userdata',
            name='lname',
            field=models.CharField(default='Unknown', max_length=20),
        ),
    ]