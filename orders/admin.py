from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'car', 'quantity', 'ordered_at']
    list_filter = ['ordered_at']
