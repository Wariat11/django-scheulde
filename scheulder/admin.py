from django.contrib import admin
from .models import Event,Service
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('service','first_name','date','time')
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name',)