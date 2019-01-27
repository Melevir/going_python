from django.urls import path

from . import views

urlpatterns = [
    path('<int:question_id>/activate/', views.activate),
]
