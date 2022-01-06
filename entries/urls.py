from django.urls import path

from .views import (
    EnrtyCreateView
)

urlpatterns = [
    path('create',EnrtyCreateView.as_view()),
]

