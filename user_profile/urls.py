from django.urls import path 
from .views import Account_type, Mini_user

urlpatterns = (
    path("account_type/", Account_type.as_view()),
    path("mini_user/", Mini_user.as_view()),
        )
