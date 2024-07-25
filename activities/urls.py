from django.urls import path
from .import views

app_name = "activities"

urlpatterns = [
    path('activities/', views.activities, name = 'activities'),
    path('activityDetail/<int:id>', views.activityDetail, name = 'activityDetail'),
]
