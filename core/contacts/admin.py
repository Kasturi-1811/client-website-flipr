from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile', 'city', 'created_at')
    search_fields = ('full_name', 'email', 'mobile', 'city')
    list_filter = ('city', 'created_at')
