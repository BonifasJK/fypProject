from django.contrib import admin
from . import models
from .models import Mitigation, RiskDetails

# Register your models here.

class RiskAdmin(admin.ModelAdmin):
    # To Sett Pagination
    list_per_page = 6
    list_max_show_all = 6
    list_display = ('title','reporter','Description', 'Details', 'status', 'last_updated', 'likelihood', 'impact', 'mitigation')

admin.site.register(models.Risk, RiskAdmin)

class UnitsAdmin(admin.ModelAdmin):
    # To Sett Paginationcl
    list_per_page = 6
    list_max_show_all = 6
    list_display = ('Units',)
admin.site.register(models.Unit, UnitsAdmin)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('fullname','role','Unit','total_risks')
admin.site.register(models.User, UsersAdmin)

admin.site.register(Mitigation)
admin.site.register(RiskDetails)

    

    