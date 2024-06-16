from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('risk-details/', views.risk_details_view, name='risk_details'),
    path('mitigation/', views.mitigation_view, name='mitigation_view'),
    path('risk/', views.risk_view, name='risk_view'),
    
]

