# Generated by Django 4.2.2 on 2023-07-31 19:56

from django.db import migrations, models
import utilities.generator


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=utilities.generator.id_generator,
                        editable=False,
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
        ),
    ]
