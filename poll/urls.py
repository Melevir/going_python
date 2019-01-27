from django.urls import path

from poll.views import ActivationView, ActiveQuestionDetailView, VoteView, StatView

urlpatterns = [
    path('<int:question_id>/activate/', ActivationView.as_view()),
    path('active/', ActiveQuestionDetailView.as_view()),
    path('<int:question_id>/vote/<int:option_id>/', VoteView.as_view()),
    path('<int:question_id>/stat/', StatView.as_view()),
]
