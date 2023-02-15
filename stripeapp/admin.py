from django.contrib import admin
from stripeapp.models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass