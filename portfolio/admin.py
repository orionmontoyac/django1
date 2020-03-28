from django.contrib import admin
from .models import Project

admin.site.register(Project)
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

