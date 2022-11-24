from django.contrib import admin
from blog.models import News, Category

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','content','is_published','photo','category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
