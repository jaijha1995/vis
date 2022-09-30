from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from myapp.resources import SignupResource , UserResource
from .models import User,Signup 

# Register your models here.

class SignupAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SignupResource


class userAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = UserResource


admin.site.register(User , userAdmin)
admin.site.register(Signup , SignupAdmin)