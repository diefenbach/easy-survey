# Generated by Django 4.2 on 2023-10-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("easy_survey", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="answer",
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name="question",
            name="content",
            field=models.JSONField(blank=True),
        ),
    ]
