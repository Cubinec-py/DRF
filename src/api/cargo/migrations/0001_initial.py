# Generated by Django 4.2.2 on 2023-06-13 18:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("location", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cargo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "weight",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=1),
                            django.core.validators.MaxValueValidator(limit_value=10000),
                        ],
                        verbose_name="Cargo load capacity",
                    ),
                ),
                (
                    "description",
                    models.TextField(max_length=250, verbose_name="Cargo description"),
                ),
                (
                    "location_delivery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cargo_delivery",
                        to="location.location",
                        verbose_name="Cargo delivery location",
                    ),
                ),
                (
                    "location_pick_up",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cargo_pick_up",
                        to="location.location",
                        verbose_name="Cargo pick-up location",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cargo",
                "verbose_name_plural": "Cargo",
            },
        ),
    ]
