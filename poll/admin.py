from django.contrib import admin
from .models import Question, Choice, Vote


class ChoiceInline(admin.StackedInline):
    model = Choice


class VoteInline(admin.StackedInline):
    model = Vote


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    inlines = [
        VoteInline,
    ]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
