# Generated by Django 4.2 on 2023-10-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("easy_survey", "0003_alter_answer_answer_alter_question_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="answer",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="question",
            name="content",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
