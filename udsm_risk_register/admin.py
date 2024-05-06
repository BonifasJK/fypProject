from django.contrib import admin
from . import models

# Register your models here.

class RiskAdmin(admin.ModelAdmin):
    # To Sett Pagination
    list_per_page = 6
    list_max_show_all = 6
<<<<<<< HEAD
    list_display = ('username','job_title','department','total_risks','status','last_updated')
=======
    list_display = ('reporter','role','unit','status','last_updated')
>>>>>>> refs/remotes/origin/main
admin.site.register(models.Risk, RiskAdmin)

class UnitsAdmin(admin.ModelAdmin):
    # To Sett Pagination
    list_per_page = 6
    list_max_show_all = 6
    list_display = ('Units',)
admin.site.register(models.Unit, UnitsAdmin)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('fullname','role','Unit','total_risks')
admin.site.register(models.User, UsersAdmin)
    

    