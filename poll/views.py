from django.http import HttpResponse
from .models import Question


def activate(request, **kwargs):
    if request.method not in ['POST', 'PUT', 'PATCH']:
        return HttpResponse(status=405)

    question = Question.objects.get(id=kwargs['question_id'])
    print(question)

    if question:
        for q in Question.objects.all():
            if q.is_active:
                q.is_active = False
                q.save()
        question.is_active = True
        question.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)
