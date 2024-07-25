from django.urls import path
from .import views

app_name = "about"

urlpatterns = [
    path('classes/', views.classes, name = 'classes'),
    path('teacher/', views.teacher, name = 'teacher'),
    path('student/', views.student, name = 'student'),
]
