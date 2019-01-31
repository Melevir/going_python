from datetime import datetime
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views import View
from poll.models import Question, Choice, Vote, UserCount
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Count, F, Q


class ActivationView(View):
    def post(self, request, **kwargs):
        question = get_object_or_404(id=kwargs['question_id'])
        Question.objects.filter(is_active=True).update(is_active=False)
        question.is_active = True
        question.activation_datetime = datetime.now()
        question.save()

        return HttpResponse()


class ActiveQuestionDetailView(View):
    def get(self, request):
        try:
            question = Question.objects.get(is_active=True)
        except ObjectDoesNotExist:
            return HttpResponseNotFound()

        choices = question.choices.all()
        options = [{'id': choice.id, 'text': choice.choice_text} for choice in choices]
        data = {
            'question_text': question.question_text,
            'question_id': question.id,
            'options': options,
        }

        return JsonResponse(data=data)


class VoteView(View):
    def post(self, request, **kwargs):
        question = get_object_or_404(Question, id=kwargs['question_id'])
        option = get_object_or_404(Choice, id=kwargs['option_id'])

        if option.question != question or not question.is_active or ('user_id' not in request.GET):
            return HttpResponseBadRequest()

        Vote.objects.create(
            choice=option,
            user_id=request.GET['user_id'],
            vote_datetime=datetime.now(),
        )

        return HttpResponse()


class StatView(View):
    def get(self, request, **kwargs):
        question = get_object_or_404(Question, id=kwargs['question_id'])
        choices = question.choices.all()
        hits = [{'id': choice.id, 'hits': choice.votes.count()} for choice in choices]
        return JsonResponse(data={'stat': hits})


class StartUserView(View):
    def get(self, request):
        UserCount.objects.filter(id=1).update(user_count=F('user_count') + 1)
        return HttpResponse()


class StartUserStatView(View):
    def get(self, request):
        data = {'total': UserCount.objects.first().user_count}
        return JsonResponse(data=data)


class NomineesView(View):
    def get(self, request):
        nominees = Vote.objects.annotate(delay=F('vote_datetime') - F('choice__question_id__activation_datetime'))
        nominees = nominees.values('user_id').annotate(
            wrong_ans=Count('choice', filter=Q(choice__is_game_over=True)),
            avg_delay=Avg('delay'),
        )
        nominees_sorted = nominees.order_by('wrong_ans', 'avg_delay')
        nominees_list = [nominee['user_id'] for nominee in nominees_sorted]
        return JsonResponse(data=nominees_list[:10], safe=False)
