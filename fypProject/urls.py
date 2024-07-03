from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from jazzmin import settings as jazzmin_settings

=======
 
>>>>>>> 3be35839 (heatmap uploaded)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add your custom URL patterns here
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('risk-register/', auth_views.register_view, name='register'),
    # Include URLs from other apps if needed
    path('', include("udsm_risk_register.urls")),
    path('udsm_risk_register/', include('udsm_risk_register.urls')),
    
  
    
]

