from django.urls import path
from .import views

app_name = "notice"

urlpatterns = [
    path('notice/', views.notice, name = 'MyNotice'),
    path('noticeDetail/<int:id>', views.noticeDetail, name = 'noticeDetail')
]
