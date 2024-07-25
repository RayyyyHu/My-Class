from django.urls import path
from .import views

app_name = "documentssharing"

urlpatterns = [
    path('documentssharing/', views.documentssharing, name = 'documentssharing'),
    path('getDoc/<int:id>', views.getDoc, name = 'getDoc')
]
