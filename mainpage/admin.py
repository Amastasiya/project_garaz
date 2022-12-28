from django.contrib import admin

from .models import Employee
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    #list_filter = ()
    list_display = [field.name for field in Employee._meta.get_fields()]
from .models import Guide
@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Guide._meta.get_fields()]

