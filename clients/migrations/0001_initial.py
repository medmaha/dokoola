# Generated by Django 4.2.2 on 2023-07-31 19:56

from django.db import migrations, models
import utilities.generator


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=utilities.generator.id_generator,
                        editable=False,
                        max_length=64,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("about", models.TextField(default="", max_length=1500)),
                ("city", models.CharField(blank=True, default="", max_length=100)),
                ("phone", models.CharField(blank=True, default="", max_length=50)),
                ("region", models.CharField(blank=True, default="", max_length=50)),
                ("address", models.CharField(blank=True, default="", max_length=120)),
                ("country", models.CharField(default="", max_length=100)),
                (
                    "zip_code",
                    models.CharField(blank=True, default="00000", max_length=20),
                ),
                ("jobs_created", models.IntegerField(default=0)),
                ("jobs_completed", models.IntegerField(default=0)),
            ],
        ),
    ]
