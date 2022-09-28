from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
from .models import skills,member
@admin.register(member)
class memberAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('id','keydata','name','post'
    )
    search_fields=('id','keydata','name')

@admin.register(skills)
class skillsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('id','keydata','skill','member'
    )
    search_fields=('id','keydata','name')