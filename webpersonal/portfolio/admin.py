from django.contrib import admin

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

from .models import Project


admin.site.register(Project, ProjectAdmin)
