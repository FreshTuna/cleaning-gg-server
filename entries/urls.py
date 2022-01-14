from django.urls import path

from .views import (
    EntryCreateView,
    EntryGetView,
)

urlpatterns = [
    path('create',EntryCreateView.as_view()),
    path('members', EntryGetView.as_view()),
]

