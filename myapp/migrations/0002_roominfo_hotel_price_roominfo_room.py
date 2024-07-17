# Generated by Django 5.0.6 on 2024-06-06 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roominfo',
            name='hotel_price',
            field=models.IntegerField(default=800),
        ),
        migrations.AddField(
            model_name='roominfo',
            name='room',
            field=models.CharField(choices=[('AC', 'ac'), ('NON-AC', 'non-ac')], default='AC', max_length=8),
        ),
    ]
