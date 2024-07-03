from django.shortcuts import render
from .models import RiskDetails, Mitigation, Risk
from .tables import RiskDetailsTable, MitigationTable, RiskTable   
from django_tables2 import RequestConfig
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm

# from bokeh.plotting import figure, show
# from bokeh.palettes import Viridis256  # Import Viridis256 palette (optional)
# from bokeh.transform import LinearColorMapper  # Import LinearColorMapper
# from .models import Risk  # Import your data model (if applicable)
# from django.db.models import Count  # Import Count function
# from datetime import date, timedelta
# from .models import Risk
# from django.utils import timezone
# from . import utils
# import plotly.graph_objects as go
from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
from django.utils import timezone
from udsm_risk_register.models import Risk
import plotly.express as px
from . import utils 

import plotly.graph_objects as go
import plotly.express as px
import calendar

# @login_required
def risks_reported(request):
    # Fetch risk data from your model, adjust filtering as per your requirement
    risks = Risk.objects.all()  # Adjust filtering as per your model's structure and needs

    # Define the color scale for the heat-map
    colorscale = [
        [0, 'green'],        # Very low (1)
        [0.2, 'yellow'],     # Low (2)
        [0.4, 'orange'],     # Moderate (3)
        [0.6, 'red'],        # High (4)
        [1, 'darkred']       # Very high (5)
    ]

    # Initialize the z matrix and risk_data
    z = [[0] * 5 for _ in range(5)]  # Initialize a 5x5 matrix with zeros
    risk_data = [[''] * 5 for _ in range(5)]  # Initialize a 5x5 matrix with empty strings

    # Populate z and risk_data based on fetched data
    for risk in risks:
        try:
            likelihood = int(risk.likelihood)  # Convert to integer
            impact = int(risk.impact)          # Convert to integer
            if 1 <= likelihood <= 5 and 1 <= impact <= 5:  # Ensure values are within range
                z[likelihood - 1][impact - 1] += 1  # Increment count at respective matrix position
                risk_data[likelihood - 1][impact - 1] += f"{risk.Risk_title}, "  # Update risk data
        except ValueError:
            # Handle cases where likelihood or impact cannot be converted to int
            pass

    # Create the heat-map
    fig = go.Figure(data=go.Heatmap(
        z=z,
        text=risk_data,
        texttemplate="%{text}",
        textfont={"size": 10},
        colorscale=colorscale,
        showscale=True))

    # Update layout to match the axes labels and title
    fig.update_layout(
        title="Risk Heat-Map showing the Overall Risk Profile for UDSM",
        xaxis=dict(title="Impact", tickvals=[0, 1, 2, 3, 4], ticktext=["Very low (1)", "Low (2)", "Moderate (3)", "High (4)", "Very High (5)"]),
        yaxis=dict(title="Likelihood", tickvals=[0, 1, 2, 3, 4], ticktext=["Rare (1)", "Unlikely (2)", "Medium (3)", "Likely (4)", "Almost Certain (5)"]),
        height=500,  # Adjust height of the heatmap
        width=800,   # Adjust width of the heatmap
    )

    # Convert the figure to HTML and pass it to the template
    chart = fig.to_html(full_html=True, include_plotlyjs=True)

    context = {'chart': chart}
    return render(request, 'risks_reported.html', context)


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