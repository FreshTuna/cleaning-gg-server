from django.urls import path

from .views import (
    MatchCreateView,
    MatchGetView,
    MatchStartView,
    MatchRandomizeView,
)

urlpatterns = [
    path('create',MatchCreateView.as_view()),
    path('list',MatchGetView.as_view()),
    path('start',MatchStartView.as_view()),
    path('randomize',MatchRandomizeView.as_view()),
]

