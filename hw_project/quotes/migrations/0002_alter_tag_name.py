# Generated by Django 4.2 on 2023-04-29 21:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
