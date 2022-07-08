from django.urls import path
from .views import Student_minimal_view, Create_student_profile_view, Detail_update_student_profile_view
from .prefect_views import Prefect_view, Prefect_detail_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #student views...
    path('', Student_minimal_view.as_view(), name='Student_min_view'),
    path('create_student/', Create_student_profile_view.as_view(), name="create student profile"),
    #Detail student view
    path('<int:pk>/',
         Detail_update_student_profile_view.as_view(),
         name='Detail student view'),
    #Prefect views...
    path('prefects/', Prefect_view.as_view(), name='All prefects'),
    path('prefects/<int:pk>/',
         Prefect_detail_view.as_view(),
         name='Detail prefects'),
]+static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )
