from django.contrib import admin
from myapp.models import Students
# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['roll_number','first_name','last_name','address','mobile']



admin.site.register(Students,StudentsAdmin)