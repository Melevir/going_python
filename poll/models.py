from django.db import models
from datetime import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    activation_datetime = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return 'Question: {0}'.format(self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    weight = models.PositiveSmallIntegerField(default=0)
    is_game_over = models.BooleanField(default=False)

    def __str__(self):
        return '{0}/{1}, {2}, votes: {3}'.format(self.question.id, self.id, self.choice_text, self.votes.count())

    class Meta:
        ordering = ['question', 'weight']


class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    user_id = models.CharField(null=False, max_length=200)
    vote_datetime = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return 'Vote: User with id {0} voted for {1}'.format(self.user_id, self.choice.choice_text)


class UserCount(models.Model):
    user_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return '# of users: {0}'.format(self.user_count)
