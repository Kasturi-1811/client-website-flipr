from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'description')
    search_fields = ('name',)
    
    def image_preview(self, obj):
        return obj.image.url if obj.image else ''
    image_preview.short_description = 'Image'
