from django.contrib import admin
from django.urls import path, include
from udsm_risk_register import views as udsm_views
urlpatterns = [
    # path('login/', ),
    path('', include("udsm_risk_register.urls")),
    path('', include('django_dyn_dt.urls')), 
    path('', include('udsm_risk_register.urls')),
]
