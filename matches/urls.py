from django.urls import path

from .views import (
    MatchCreateView
)

urlpatterns = [
    path('create',MatchCreateView.as_view()),
]

