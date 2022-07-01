from django.urls import path
from .views import All_Staff_View, Detail_Staff_View, Register_Staff_View, Basic_staff_view, Detailed_basic_staff_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', All_Staff_View.as_view(), name="All Staff"),
    path('basic/', Basic_staff_view.as_view(), name="Basic staff"),
    path('basic/<int:pk>/', Detailed_basic_staff_view.as_view(), name="Detailed Basic Staff"),
    path('<int:pk>/', Detail_Staff_View.as_view(), name="Detail"),
    path('register/', Register_Staff_View.as_view(), name="Register"),
]
# for the images.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
