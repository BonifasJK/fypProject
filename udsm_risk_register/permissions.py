from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from .models import Mitigation, RiskDetails, User, Risk

User = get_user_model()

def setup_permissions():
    # Create the group if it doesn't exist
    risk_manager_group, created = Group.objects.get_or_create(name='RiskManager')
    
      # Create or get the RiskChampion group
    risk_champion_group, created = Group.objects.get_or_create(name='RiskChampion')
        
    # Get or create the permissions for Mitigation, RiskDetails, Risk models
    models = {
        'RiskManager': [Mitigation, RiskDetails, Risk],
        'RiskChampion': [Risk]
    }
    
    for group_name, model_list in models.items():
        group = Group.objects.get(name=group_name)
        for model in model_list:
            content_type = ContentType.objects.get_for_model(model)
            permissions = Permission.objects.filter(content_type=content_type)
            for perm in permissions:
                group.permissions.add(perm)
    
    # Ensure all staff users are in their respective groups
    staff_users = User.objects.filter(is_staff=True)
    for user in staff_users:
        if user.groups.filter(name='RiskManager').exists():
            user.groups.add(risk_manager_group)
        elif user.groups.filter(name='RiskChampion').exists():
            user.groups.add(risk_champion_group)
        user.save()
# Call the setup function to apply changes
setup_permissions()
