from django.urls import path

from .views import (
    EntryCreateView,
    EntryGetView,
    EntryDeleteView,
    EntryLeaderView,
)

urlpatterns = [
    path('create',EntryCreateView.as_view()),
    path('members', EntryGetView.as_view()),
    path('delete', EntryDeleteView.as_view()),
    path('leader', EntryLeaderView.as_view()),
]

