from django.contrib import admin
from .models import honor

# Register your models here.

admin.site.site_header = '联合班级网站后台管理系统'
admin.site.site_title = '联合班级网站后台管理系统'

admin.site.register(honor)
