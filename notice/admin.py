from django.contrib import admin
from .models import MyNotice

# Register your models here.

class MyNoticeAdmin(admin.ModelAdmin):
    style_fields = {'description': 'ueditor'}

admin.site.register(MyNotice, MyNoticeAdmin)
