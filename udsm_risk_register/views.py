from django.shortcuts import render
from .models import RiskDetails, Mitigation, Risk
from .tables import RiskDetailsTable, MitigationTable, RiskTable   
from django_tables2 import RequestConfig
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm


#Home Page
def home(request):
    return render(request, "home.html")

# #Login Page
# def login(request):
#     return render(request, "login.html")



# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')  # Redirect to Django admin
#     return render(request, 'login.html')



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = request.POST.get('remember_me')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_staff or user.is_superuser:
                    
                    # Set session expiry time based on Remember Me checkbox
                    if remember_me:
                        # Set a longer session expiry time (e.g., 30 days)
                        request.session.set_expiry(2592000)  # 30 days in seconds

                    return redirect('/admin/')  # Redirect staff and superusers to Django admin
                else:
                    return redirect('/')  # Redirect non-staff users to home or another page
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



# def is_staff_user(user):
#     return user.is_staff

# @user_passes_test(is_staff_user)
# def staff_dashboard(request):
#     # You can add any context data you want to display in the staff dashboard
#     return render(request, 'staff_dashboard.html')

# @staff_member_required
# def staff_dashboard(request):
#     return render(request, 'staff_dashboard.html')
    
# def risk_details_view(request):
#     table = RiskDetailsTable(RiskDetails.objects.all())
#     RequestConfig(request).configure(table)
#     return render(request, 'udsm_risk_register/risk_details_template.html', {'table': table})

# def mitigation_view(request):
#     table = MitigationTable(Mitigation.objects.all())
#     RequestConfig(request).configure(table)
#     return render(request, 'udsm_risk_register/mitigation_template.html', {'table': table})

# def risk_view(request):
    table = RiskTable(Risk.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'templateudsm_risk_register/risk_template.html', {'table': table})
    queryset = Risk.objects.all()
    table = RiskTable(queryset)
    return render(request, 'udsm_risk_register/risk_template.html', {'table': table})

#  def register(request):
#      return render(request, 'udsm_risk_register/register.html')