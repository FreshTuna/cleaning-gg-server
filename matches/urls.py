from django.urls import path

from .views import (
    MatchCreateView,
    MatchGetView,
)

urlpatterns = [
    path('create',MatchCreateView.as_view()),
    path('list',MatchGetView.as_view()),
]

