from django.contrib import admin
from .models import Blog, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'title',]
    list_display_links = ['id', 'title',]

class BlogAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'created', 'updated']
    list_display_links = ['id', 'title']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
