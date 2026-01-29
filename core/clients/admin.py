from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image_preview')
    search_fields = ('name', 'designation')
    list_filter = ('designation',)

    def image_preview(self, obj):
        return obj.image.url if obj.image else ''
    image_preview.short_description = 'Image'
