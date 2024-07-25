from django.contrib import admin
from .models import MyActivity

# Register your models here.

class MyActivityAdmin(admin.ModelAdmin):
    style_fields = {'description': 'ueditor'}

admin.site.register(MyActivity, MyActivityAdmin)
