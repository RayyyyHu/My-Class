from django.urls import path
from .import views

app_name = "honor"

urlpatterns = [
    path('honor/<str:honorName>/', views.Honor, name = 'honor')
]
