# Generated by Django 5.0.4 on 2024-05-01 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Column",
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
                ("name", models.CharField(max_length=200)),
                ("length", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="UserLogin",
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
                ("email", models.EmailField(max_length=100)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="UserSignup",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
                ("password", models.CharField(max_length=50)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Card",
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
                ("title", models.CharField(max_length=200)),
                ("order", models.IntegerField(default=0)),
                (
                    "column",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cards",
                        to="api.column",
                    ),
                ),
            ],
        ),
    ]