from django.contrib import admin
from testapp.models import employee
# Register your models here.

class employeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','ecity','esalary']

admin.site.register(employee,employeeAdmin)
