from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('accounts/login', views.login, name='login'),
    # path('risk-details/', views.risk_details_view, name='riskdetails'),
    # path('mitigation/', views.mitigation_view, name='mitigationview'),
    # path('risk/', views.risk_view, name='riskview'),
    
]

