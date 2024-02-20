# from django.contrib import admin
# from .models import Category

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'title', 'created_at', 'updated_at', 'user')
#     search_fields = ('name', 'description', 'title', 'user__username')
#     list_filter = ('created_at', 'updated_at', 'user__username')

from django.contrib import admin
from .models import Category

admin.site.register(Category)