# Generated by Django 5.0.4 on 2024-05-01 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_rename_usersignup_userdetails_delete_userlogin_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="card",
            name="order",
        ),
        migrations.AlterField(
            model_name="card",
            name="column",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.column"
            ),
        ),
    ]