from django.contrib import admin
from .models import Market,Commodity,Commodity_type,Visit,Description
# Register your models here.

class Commodity_type_Admin(admin.ModelAdmin):
    list_display = ['visit_day','commodity_type','name','num_pieces','weight_volume','price']
    list_filter = ['commodity_type__name']
    search_fields = ['commodity_type__name','name']
admin.site.register(Market)
admin.site.register(Commodity)
admin.site.register(Commodity_type,Commodity_type_Admin)
admin.site.register(Visit)
admin.site.register(Description)
