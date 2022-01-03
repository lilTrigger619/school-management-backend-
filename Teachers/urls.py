from django.urls import path
from .views import All_Staff_View, Detail_Staff_View, Register_Staff_View

urlpatterns = [
 path('', All_Staff_View.as_view(), name="All Staff"),
 path('<int:pk>', Detail_Staff_View.as_view(), name="Detail"),
 path('register', Register_Staff_View.as_view(), name="Register"),
        ]
