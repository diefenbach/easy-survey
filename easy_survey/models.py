from django import forms
from django.db import models


class Survey(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Question(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.JSONField(blank=True, default=dict)
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="questions"
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.JSONField(blank=True, default=dict)
