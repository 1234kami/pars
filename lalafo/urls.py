from django.urls import path
from . import views

urlpatterns = [
    path("admin", views.LalafoItemAPIView.as_view()),
]