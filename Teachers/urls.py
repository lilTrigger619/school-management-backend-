from django.urls import path
from .views import Register_Staff_View, Detail_Staff_View 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
 path('/', Register_Staff_View.as_view(), name="Register"),
 path('<int:pk>/', Detail_Staff_View.as_view(), name="Detail"),
 path('login/', TokenObtainPairView.as_view(), name='login'),
 path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
 path('verify_token/', TokenVerifyView.as_view(), name='verify_token'),
        ]
