from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from poll.views import ActivationView, ActiveQuestionDetailView, VoteView, StatView, NomineesView

urlpatterns = [
    path('<int:question_id>/activate/', csrf_exempt(ActivationView.as_view())),
    path('active/', ActiveQuestionDetailView.as_view()),
    path('<int:question_id>/vote/<int:option_id>/', csrf_exempt(VoteView.as_view())),
    path('<int:question_id>/stat/', StatView.as_view()),
    path('nominees/', NomineesView.as_view()),
]
