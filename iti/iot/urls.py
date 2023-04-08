from django.urls import path
from iot import views

urlpatterns = [
    path('home/', views.home),
    path('student/<st_id>', views.getStudent),
    path('allstu/', views.getAllStudents),
    path('new/', views.newStudent),
    path('edit/<st_id>', views.editStudent),
    path('delete/<st_id>', views.deleteStudent)
    
]