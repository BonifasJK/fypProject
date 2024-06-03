from django.contrib import admin
from . import models
from .models import Mitigation, RiskDetails, User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserAdmin(UserAdmin):
    model = User
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('username', 'password1', 'password2', 'fullname', 'role', 'unit'),
        }),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('fullname', 'role', 'unit')}),
    )
    list_display = ['username', 'email', 'fullname', 'role', 'unit']

admin.site.register(User, CustomUserAdmin)

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

admin.site.register(Mitigation)
admin.site.register(RiskDetails)

    

    