from django.contrib import admin
from .models import Question, Choice, Vote


class ChoiceInline(admin.StackedInline):
    model = Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
