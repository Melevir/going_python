from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views import View
from poll.models import Question, Choice, Vote
from django.core.exceptions import ObjectDoesNotExist


class ActivationView(View):
    def post(self, request, **kwargs):
        try:
            question = Question.objects.get(id=kwargs['question_id'])
        except ObjectDoesNotExist:
            return HttpResponseNotFound()

        Question.objects.filter(is_active=True).update(is_active=False)
        question.is_active = True
        question.save()

        return HttpResponse()


class ActiveQuestionDetailView(View):
    def get(self, request):
        try:
            question = Question.objects.get(is_active=True)
        except ObjectDoesNotExist:
            HttpResponseNotFound()

        choices = question.choices.all()
        options = [{'id': choice.id, 'text': choice.choice_text} for choice in choices]
        data = {
            'question_text': question.question_text,
            'options': options,
        }

        return JsonResponse(data=data)


class VoteView(View):
    def post(self, request, **kwargs):
        try:
            question = Question.objects.get(id=kwargs['question_id'])
            option = Choice.objects.get(id=kwargs['option_id'])
        except ObjectDoesNotExist:
            return HttpResponseNotFound()

        if option.question != question or not question.is_active or ('user_id' not in request.GET):
            return HttpResponseBadRequest()

        Vote.objects.create(choice=option, user_id=request.GET['user_id'])

        return HttpResponse()
