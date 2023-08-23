# from django.contrib import admin
#
# # Register your models here.
# # tạo cái này để vào admin site, có thể thêm xoá sửa vào database
# from .models import Category, Post
#
# admin.site.register(Post)
# admin.site.register(Category)
from django.contrib import admin
from . import models


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.Category)