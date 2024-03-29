# Generated by Django 4.2.7 on 2023-11-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trafficdata',
            name='data',
        ),
        migrations.AddField(
            model_name='trafficdata',
            name='average_speed',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trafficdata',
            name='vehicle_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trafficdata',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
