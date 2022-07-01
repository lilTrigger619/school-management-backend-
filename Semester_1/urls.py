from django.urls import path
from .views import Sem_1_view

urlpatterns = [
    path('', Sem_1_view.as_view()),
    path('<int:pk>/', Sem_1_detail_view.as_view()),
        ]
