from django.contrib import admin
from . import models

# Register your models here.

class UnitsAdmin(admin.ModelAdmin):
    # To Sett Pagination
    list_per_page = 6
    list_max_show_all = 6
    list_display = ('Units',)
admin.site.register(models.Units, UnitsAdmin)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('Fullname','JobTitle','Unit','TotalRisk')
admin.site.register(models.User, UsersAdmin)
    

    