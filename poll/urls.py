from django.urls import path

from poll.views import Activation, ActiveQuestion

urlpatterns = [
    path('<int:question_id>/activate/', Activation.as_view()),
    path('active/', ActiveQuestion.as_view()),
]
