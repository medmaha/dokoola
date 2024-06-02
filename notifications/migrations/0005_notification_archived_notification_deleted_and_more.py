# Generated by Django 5.0.2 on 2024-06-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_alter_notification_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]