
from django.urls import path
from .views import Level_view, Detailed_level_view

urlpatterns = [
    path('', Level_view.as_view()),
    path('<int:pk>/', Detailed_level_view.as_view()),
]
