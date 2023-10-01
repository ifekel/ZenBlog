from django.contrib import admin
from .models import Category, Blog, BlogImage


class BlogImageInline(admin.TabularInline):
    model = BlogImage


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    inlines = [
        BlogImageInline
    ]
    list_display = ['category', 'title', 'body']


admin.site.register(Blog, BlogAdmin)
