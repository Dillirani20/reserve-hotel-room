# Generated by Django 5.0.6 on 2024-06-08 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_bookinginfo_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billinginfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.IntegerField()),
                ('hotel_price', models.IntegerField()),
                ('pay', models.CharField(choices=[('UPI', 'upi'), ('NET BANKING', 'net banking'), ('DEBIT CARD', 'debit card'), ('CREDIT CARD', 'credit card')], max_length=20, unique=True)),
            ],
        ),
    ]
