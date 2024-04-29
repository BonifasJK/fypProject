from django.contrib import admin
from . import models

# Register your models here.

class UnitsAdmin(admin.ModelAdmin):
    list_display = ('Units',)
admin.site.register(models.Units, UnitsAdmin)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('Fullname','JobTitle','Department','TotalRisk')
admin.site.register(models.Users, UsersAdmin)
    

    