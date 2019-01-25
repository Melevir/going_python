from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user_id = models.CharField(null=False, max_length=200)
