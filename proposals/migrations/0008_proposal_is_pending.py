# Generated by Django 5.0.2 on 2024-05-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0007_proposal_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='is_pending',
            field=models.BooleanField(default=True),
        ),
    ]
