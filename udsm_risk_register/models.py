from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group


UnitList = (
    ('Human Resource', 'Human Resource'),
    ('CoICT', 'CoICT'),
    ('CoET', 'CoET'),
    ('SoED', 'SoED'),
    ('CoHU', 'CoHU'),
    ('SoAF', 'SoAF'),
    ('CoAF', 'CoAF'),
    ('CoNAS', 'CoNAS'),
    ('CoSS', 'CoSS'),
    ('IDS', 'IDS'),
    ('UDSoL', 'UDSoL'),
    ('SJMC', 'SJMC'),
    ('SoMG', 'SoMG'),
    ('UDSE', 'UDSE'),
    ('IKS', 'IKS'),
)

Objectives =(
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E')
)

categories = (
    ('Governance', 'Governance'),
    ('Health Safety and welfare', 'Health Safety and welfare'),
    ('Fraud and Corruption', 'Fraud and Corruption'),
    ('Research and consultancy', 'Research and consultancy'),
    ('Academic', 'Academic'),
    ('Compliance', 'Compliance'),
    ('Human Capital', 'Human Capital'),
    ('ICT', 'ICT'),
    ('Gender', 'Gender'),
    ('Infrastructure Management', 'Infrastructure Management'),
    ('Operational', 'Operational')
)
Role = (
    ('RiskManager', 'RiskManager'),
    ('RiskChampion', 'RiskChampion'),
)

StatusList = (
    ('pending', 'pending'),
    ('approved', 'approved'),

)

impacts = (
    ('Very high', 'Very High'),
    ('High', 'High'),
    ('Moderate', 'Moderate'),
    ('Low', 'Low'),
    ('Very Low', 'Very Low'),
)

ids = (
    ('C1', 'C1'),
    ('C2', 'C2'),
    ('C3', 'C3'),
    ('C4', 'C4'),
)

effectiveness = (
    ('Effective', 'Effective'),
    ('Partial Effective', 'Partial Effective'),
    ('Ineffective', 'Ineffective')
)
class Unit(models.Model):
    Unit_id = models.AutoField(primary_key=True, null=False)
    Units = models.CharField(max_length=100, choices=UnitList)

    def __str__(self):
        return self.Units

class Mitigation(models.Model):
    id = models.AutoField(primary_key=True)
    mitigation = models.TextField(max_length=400)
    effectiveness = models.CharField(max_length=400, choices=effectiveness)
    weakness = models.CharField(max_length=400)

    def __str__(self):
        return self.mitigation

class RiskDetails(models.Model):
    id = models.AutoField(primary_key=True)
    Causes = models.TextField(max_length=400)
    consequences = models.TextField(max_length=500)

    def __str__(self):
        return self.Causes

class User(AbstractUser):
    email = models.EmailField() 
    id = models.AutoField(primary_key=True, default=None)
    role = models.CharField(max_length=25, choices=Role, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)

    @property
    def TotalRisk(self):
        return self.risk_set.count()

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        swappable = 'AUTH_USER_MODEL'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.get_full_name()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role:
            group, created = Group.objects.get_or_create(name=self.role)
            self.groups.add(group)

class Risk(models.Model):
    Objective = models.CharField(max_length=20, choices=Objectives, verbose_name='Objective Code', null=True)
    RiskCategory = models.CharField(max_length=100, choices=categories, verbose_name='Risk Category', null=True)
    title = models.CharField(max_length=200, verbose_name='Risk Title')
    RiskID = models.CharField(max_length=20, verbose_name='Risk ID', null=True, unique=True, blank=True)
    Description = models.CharField(max_length=400, verbose_name='Risk Description')
    Details = models.ForeignKey(RiskDetails, on_delete=models.CASCADE, verbose_name='Risk Details')
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likelihood = models.CharField(max_length=50, choices=impacts)
    impact = models.CharField(max_length=30, choices=impacts)
    Priority = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=10, choices=StatusList, default='pending')
    last_updated = models.DateTimeField(auto_now=True)
    approving_manager = models.ForeignKey(User, related_name='approved_risks', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Approving manager')
    def has_view_permission(self, request, obj=None):
        return request.user.is_staff or super().has_view_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff or super().has_change_permission(request, obj)
    
    def calculate_risk_score(self):
        # Map impact and likelihood to numerical values
        impact_map = {
            'Very Low': 1,
            'Low': 2,
            'Moderate': 3,
            'High': 4,
            'Very High': 5,
        }
        
        likelihood_map = {
            'Very Low': 1,
            'Low': 2,
            'Moderate': 3,
            'High': 4,
            'Very High': 5,
        }
        
        # Calculate risk score
        impact_value = impact_map.get(self.impact, 1)  # Default to 1 if not found
        likelihood_value = likelihood_map.get(self.likelihood, 1)  # Default to 1 if not found
        risk_score = impact_value * likelihood_value
        return risk_score
    
    def determine_priority(self):
        risk_score = self.calculate_risk_score()
        
        # Determine priority based on risk score
        if risk_score <= 3:
            return 'Very Low'
        elif risk_score <= 8:
            return 'Low'
        elif risk_score <= 10:
            return 'Moderate'
        elif risk_score <= 15:
            return 'High'
        else:
            return 'Very High'
    
    def save(self, *args, **kwargs):
        if not self.RiskID:
            # Calculate the next RiskID based on the Objective
            last_id = Risk.objects.filter(Objective=self.Objective).order_by('-RiskID').first()
            if last_id:
                last_id = last_id.RiskID
                prefix = self.Objective
                num = int(last_id[len(prefix):]) + 1
                new_id = f"{prefix}{num}"
            else:
                new_id = f"{self.Objective}1"
            
            self.RiskID = new_id
        self.Priority = self.determine_priority() 
        
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title} reported by {self.reporter.get_full_name()}"




    
