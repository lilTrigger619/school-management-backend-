from django.urls import path
from .views import All_Staff_View, Detail_Staff_View, Register_Staff_View, Get_User_View
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path('', All_Staff_View.as_view(), name="All Staff"),
 path('<int:pk>/', Detail_Staff_View.as_view(), name="Detail"),
 path('register/', Register_Staff_View.as_view(), name="Register"),
 path('self/', Get_User_View.as_view(), name='Get Request user'),
        ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
