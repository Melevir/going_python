from django.http import HttpResponse, JsonResponse
from django.views import View
from poll.models import Question, Choice


class Activation(View):
    def post(self, request, **kwargs):
        question = Question.objects.get(id=kwargs['question_id'])
        if question:
            Question.objects.filter(is_active=True).update(is_active=False)
            question.update(is_active=True)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)


class ActiveQuestion(View):
    def get(self, request):
        question = Question.objects.filter(is_active=True).last()
        if question:
            choices = Choice.objects.filter(question=question.id)
            options = [{'id': choice.id, 'text': choice.choice_text} for choice in choices]
            data = {
                'question_text': question.question_text,
                'options': options,
            }
            return JsonResponse(status=200, data=data)
        else:
            return HttpResponse(status=404)
