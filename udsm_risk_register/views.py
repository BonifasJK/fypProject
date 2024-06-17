from django.shortcuts import render
from .models import RiskDetails, Mitigation, Risk
from .tables import RiskDetailsTable, MitigationTable, RiskTable   
from django_tables2 import RequestConfig

#Home Page
def home(request):
    return render(request, "home.html")

#Login Page
def login(request):
    return render(request, "login.html")


# def is_staff_user(user):
#     return user.is_staff

# @user_passes_test(is_staff_user)
# def staff_dashboard(request):
#     # You can add any context data you want to display in the staff dashboard
#     return render(request, 'staff_dashboard.html')

# @staff_member_required
# def staff_dashboard(request):
#     return render(request, 'staff_dashboard.html')\
    
def risk_details_view(request):
    table = RiskDetailsTable(RiskDetails.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'udsm_risk_register/risk_details_template.html', {'table': table})

def mitigation_view(request):
    table = MitigationTable(Mitigation.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'udsm_risk_register/mitigation_template.html', {'table': table})

def risk_view(request):
    table = RiskTable(Risk.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'udsm_risk_register/risk_template.html', {'table': table})
    queryset = Risk.objects.all()
    table = RiskTable(queryset)
    return render(request, 'udsm_risk_register/risk_template.html', {'table': table})