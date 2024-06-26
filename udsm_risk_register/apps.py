from django.apps import AppConfig


class UdsmRiskRegisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'udsm_risk_register'
    
    def ready(self):
        # Import and run the permission setup
        from .permissions import setup_permissions
        setup_permissions()
    verbose_name = 'UDSM RISK MANAGEMENT'
