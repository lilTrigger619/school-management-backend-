from django.urls import path
from .views import Course_view, Detailed_course_view

urlpatterns = [
    path('', Course_view.as_view()),
    path('<int:pk>/', Detailed_course_view.as_view()),
]
