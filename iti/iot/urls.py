from django.urls import path
from iot import views

urlpatterns = [
    path('home/', views.home),
    path('student/<st_id>', views.getStudent),
    path('allstu/', views.getAllStudents),
]