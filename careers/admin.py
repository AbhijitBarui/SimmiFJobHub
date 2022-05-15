from email.mime import application
from django.contrib import admin
from .models import Jobs,Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name')

admin.site.register(Jobs)
admin.site.register(Application,ApplicationAdmin)