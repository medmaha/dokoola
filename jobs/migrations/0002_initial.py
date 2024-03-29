# Generated by Django 4.2.2 on 2023-07-31 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("jobs", "0001_initial"),
        ("proposals", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="activities",
            name="proposals",
            field=models.ManyToManyField(
                related_name="job_proposals", to="proposals.proposal"
            ),
        ),
    ]
