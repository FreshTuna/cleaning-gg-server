from django.urls import path

from .views import (
    EnrtyCreateView,
    EntryGetView,
)

urlpatterns = [
    path('create',EnrtyCreateView.as_view()),
    path('members', EntryGetView.as_view()),
]

