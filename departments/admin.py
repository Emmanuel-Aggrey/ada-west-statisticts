from django.contrib import admin
from .models import  Departmant,Department_Data,Indicator,Baseline,Report,Description
# Register your models here.

admin.site.register(Departmant)
admin.site.register(Indicator)
admin.site.register(Description)
admin.site.register(Baseline)
admin.site.register(Report)
# admin.site.register()


# class Department_Data_Admin(admin.ModelAdmin):
#     list_display = ['department','indicators','base_line','date']
#     list_editable = ['base_line']
#     search_fields =['department__name','indicators']
#     list_filter =['date_add','department']
# admin.site.register(Department_Data,Department_Data_Admin)
