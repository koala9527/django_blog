from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_time']

# 把新增的 PostAdmin 也注册进来
admin.site.register(Comment,PostAdmin)
