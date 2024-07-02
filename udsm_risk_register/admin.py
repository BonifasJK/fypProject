from django.contrib import admin
from django import forms
from django.http import HttpResponse
from io import BytesIO
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from . import models
from .models import Mitigation, RiskDetails, User, Risk
from django.utils.timezone import make_naive
from datetime import datetime 
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Custom User Admin
class CustomUserAdmin(BaseUserAdmin):
    model = User
    add_fieldsets = (
        (None, {
            'fields': ('username','email', 'password1', 'password2', 'first_name', 'last_name', 'role', 'unit'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'role', 'unit')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ['username', 'email', 'get_full_name', 'role', 'unit']
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_full_name.short_description = 'Full Name'

admin.site.register(User, CustomUserAdmin)

# Export functions

def export_as_excel(queryset):
    data = []
    for risk in queryset:
        row = {
            'Title': risk.title,
            'Description': risk.Description,
            'Reporter': f"{risk.reporter.first_name} {risk.reporter.last_name}",
            'Unit': risk.reporter.unit if hasattr(risk.reporter, 'unit') else '',
            'Mitigation': f"Mitigation: {risk.mitigation.mitigation}\nEffectiveness: {risk.mitigation.effectiveness}\nWeakness: {risk.mitigation.weakness}",
            # Add more fields as needed
        }
        data.append(row)

    df = pd.DataFrame(data)
    if 'last_updated' in df.columns:
        df.drop(columns=['last_updated'], inplace=True)

    with BytesIO() as buffer:
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name="Sheet1", index=False)
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="risks_export.xlsx"'
        return response

def export_as_pdf(queryset):
    model = queryset.model
    meta = model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={meta.verbose_name_plural}.pdf'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    data = []
    data.append(['ID'] + field_names)

    for obj in queryset:
        row = [str(obj.id)] + [str(getattr(obj, field)) for field in field_names]
        data.append(row)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ])

    table = Table(data)
    table.setStyle(style)

    elements = []
    elements.append(table)
    doc.build(elements)

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

# Export views
@staff_member_required
def export_all_as_excel(request):
    queryset = models.Risk.objects.all()
    return export_as_excel(queryset)

@staff_member_required
def export_all_as_pdf(request):
    queryset = models.Risk.objects.all()
    return export_as_pdf(queryset)

# Risk admin


class RiskAdmin(admin.ModelAdmin):
    list_per_page = 6
    list_max_show_all = 6
    list_display = ('title', 'get_reporter_full_name', 'Description', 'Details', 'status', 'likelihood', 'impact', 'mitigation')
    actions = ['export_as_excel_action', 'export_as_pdf_action']
    
    def get_reporter_full_name(self, obj):
        return f"{obj.reporter.first_name} {obj.reporter.last_name}"
    get_reporter_full_name.short_description = 'Reporter'

    def export_as_excel_action(self, request, queryset):
        return export_as_excel(queryset)
    export_as_excel_action.short_description = "Export selected items as Excel"

    def export_as_pdf_action(self, request, queryset):
        return export_as_pdf(queryset)
    export_as_pdf_action.short_description = "Export selected items as PDF"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('export/excel/', self.admin_site.admin_view(export_all_as_excel), name='risk_export_excel'),
            path('export/pdf/', self.admin_site.admin_view(export_all_as_pdf), name='risk_export_pdf'),
        ]
        return custom_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_buttons'] = [
            {'url': 'export/excel/', 'label': 'Export All as Excel'},
            {'url': 'export/pdf/', 'label': 'Export All as PDF'},
        ]
        return super().changelist_view(request, extra_context=extra_context)

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     if not obj:  # if creating a new instance
    #         form.base_fields['reporter'].widget = admin.widgets.AdminTextInputWidget()  # Use TextInput widget
    #         form.base_fields['reporter'].disabled = True  # Disable the input field
    #     return form
    def save_model(self, request, obj, form, change):
        if not obj.reporter_id:
            obj.reporter = request.user
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # if creating a new instance
            # Set choices for reporter field with only current user
            form.base_fields['reporter'].queryset = form.base_fields['reporter'].queryset.filter(pk=request.user.pk)
        return form


admin.site.register(models.Risk, RiskAdmin)

# Other admin registrations
class UnitsAdmin(admin.ModelAdmin):
    list_per_page = 6
    list_max_show_all = 6
    list_display = ('Units',)

admin.site.register(models.Unit, UnitsAdmin)
admin.site.register(Mitigation)
admin.site.register(RiskDetails)