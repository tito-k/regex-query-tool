from django.urls import path
from .views import RegexQueryView

urlpatterns = [
    path('regex-query/', RegexQueryView.as_view()),
]
