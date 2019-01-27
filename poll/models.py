from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return 'Question: {0}'.format(self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    weight = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return 'Choice: {0}, # of votes: {1}'.format(self.choice_text, self.votes.count())

    class Meta:
        ordering = ['weight']


class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    user_id = models.CharField(null=False, max_length=200)

    def __str__(self):
        return 'Vote: User with id {0} voted for {1}'.format(self.user_id, self.choice.choice_text)
