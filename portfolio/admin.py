from django.contrib import admin
from .models import ContactUS


@admin.register(ContactUS)
class ContactUSAdmin(admin.ModelAdmin):
    list_display = ["created","name","subject","message","email"]
    search_fields = ["name","email"]
    list_filter = ["created"]
