from django.urls import path
from .views import Student_account_view, Detailed_student_account_view, Activate_user_account, Deactivate_user_account, Staff_account_view, Detailed_staff_account_view

urlpatterns = [
    path('student_account/', Student_account_view.as_view()),
    path('student_account/<int:pk>/', Detailed_student_account_view.as_view()),
    path('staff_account/', Staff_account_view.as_view()),
    path('staff_account/<int:pk>/', Detailed_staff_account_view.as_view()),
    path('activate/<int:pk>/', Activate_user_account.as_view()),
    path('deactivate/<int:pk>/', Deactivate_user_account.as_view()),
]
