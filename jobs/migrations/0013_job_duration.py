# Generated by Django 5.0.2 on 2024-05-27 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_job_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='duration',
            field=models.CharField(blank=True, default='1 week', max_length=1000),
        ),
    ]
