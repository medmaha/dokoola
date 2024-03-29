# Generated by Django 4.2.2 on 2023-08-15 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proposals", "0003_proposal_is_accepted"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="proposal",
            name="hourly_rate",
        ),
        migrations.AddField(
            model_name="proposal",
            name="is_decline",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="proposal",
            name="is_reviewed",
            field=models.BooleanField(default=False),
        ),
    ]
