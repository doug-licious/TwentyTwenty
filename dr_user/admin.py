from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import DR_User
from .resources import DR_UserResource

admin.site.register(DR_User)


class DR_UserAdmin(ImportExportModelAdmin):
    resource_class = DR_UserResource
