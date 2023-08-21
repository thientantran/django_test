from django.contrib import admin

# Register your models here.
# tạo cái này để vào admin site, có thể thêm xoá sửa vào database
from .models import Category, Post

admin.site.register(Post)
admin.site.register(Category)