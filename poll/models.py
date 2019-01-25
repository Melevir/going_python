from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return 'Question: {}'.format(self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return 'Choice: {}'.format(self.choice_text)


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user_id = models.CharField(null=False, max_length=200)

    def __str__(self):
        return 'Vote: User with id {} voted for {}'.format(self.user_id, self.choice.choice_text)
