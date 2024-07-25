from django.urls import path
from .import views

app_name = "subjectscenter"

urlpatterns = [
    path('subjectscenter/<str:subjectName>', views.subjects, name = 'subjects'),
    path('subjectDetail/<int:id>', views.subjectDetail, name = 'subjectDetail'),
]
