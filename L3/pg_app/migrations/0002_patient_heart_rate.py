# Generated by Django 5.0.1 on 2024-02-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pg_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="heart_rate",
            field=models.IntegerField(default=50),
        ),
    ]
