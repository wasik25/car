from django.contrib import admin
from .models import Car, Comment

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'quantity']
    list_filter = ['brand']
    search_fields = ['name', 'brand__name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'car', 'created_at']
    search_fields = ['name', 'car__name']
