from django.contrib import admin
from .models import MySubject

# Register your models here.

class MySubjectAdmin(admin.ModelAdmin):
    style_fields = {'description': 'ueditor'}

admin.site.register(MySubject)
