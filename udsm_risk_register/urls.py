from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('accounts/login', views.login, name='login'),
<<<<<<< HEAD
    # path('risk-register', views.register, name='register')
=======
    # path('heatmap/', views.heatmap_view, name='heatmap'),
    path('risks-reported/', views.risks_reported, name='risks_reported'),
    #  path('heatmap/', views.generate_heatmap, name='heatmap'), 
>>>>>>> 3be35839 (heatmap uploaded)
    # path('risk-details/', views.risk_details_view, name='riskdetails'),
    # path('mitigation/', views.mitigation_view, name='mitigationview'),
    # path('risk/', views.risk_view, name='riskview'),
    
]

