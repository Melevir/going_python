from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views import View
from poll.models import Question, Choice, Vote
from django.views.decorators.clickjacking import xframe_options_exempt


class ActivationView(View):
    def post(self, request, **kwargs):
        question = Question.objects.get(id=kwargs['question_id'])

        if not question:
            return HttpResponseNotFound

        Question.objects.filter(is_active=True).update(is_active=False)
        question.update(is_active=True)

        return HttpResponse()


class ActiveQuestionDetailView(View):
    def get(self, request):
        question = Question.objects.get(is_active=True)

        if not question:
            return HttpResponseNotFound

        choices = question.choices.all()
        options = [{'id': choice.id, 'text': choice.choice_text} for choice in choices]
        data = {
            'question_text': question.question_text,
            'options': options,
        }

        return JsonResponse(data=data)


class VoteView(View):
    def post(self, request, **kwargs):
        question = Question.objects.get(id=kwargs['question_id'])
        option = Choice.objects.get(id=kwargs['option_id'])

        if not (question and option):
            return HttpResponseNotFound()

        if option.question != question or not question.is_active:
            return HttpResponseBadRequest()

        try:
            user_id = request.GET['user_id']
        except KeyError:
            return HttpResponseBadRequest()

        vote = Vote(choice=option, user_id=user_id)
        vote.save()
        return HttpResponse()

