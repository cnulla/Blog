from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
