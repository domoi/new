from django.contrib import admin
from blog.models import News, Category, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','content','is_published','photo','category','author']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Comment)
