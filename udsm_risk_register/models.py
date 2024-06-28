from django.contrib.auth.models import AbstractUser
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

Role = (
    ('RiskManager', 'RiskManager'),
    ('RiskChampion', 'RiskChampion'),
)

StatusList = (
    ('Submitted', 'Submitted'),
    ('Active', 'Active'),
    ('Pending', 'Pending'),
    ('Resolved', 'Resolved'),
    ('Closed', 'Closed')
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

class Unit(models.Model):
    Unit_id = models.AutoField(primary_key=True, null=False)
    Units = models.CharField(max_length=100, choices=UnitList)

    def __str__(self):
        return self.Units

class Mitigation(models.Model):
    id = models.AutoField(primary_key=True)
    mitigation = models.CharField(max_length=400)
    effectiveness = models.CharField(max_length=400)
    weakness = models.CharField(max_length=400)

    def __str__(self):
        return self.mitigation

class RiskDetails(models.Model):
    id = models.AutoField(primary_key=True)
    Causes = models.CharField(max_length=400)
    consequences = models.CharField(max_length=500)

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
    title = models.CharField(max_length=200)
    Description = models.CharField(max_length=400)
    Details = models.ForeignKey(RiskDetails, on_delete=models.CASCADE)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likelihood = models.CharField(max_length=50, choices=impacts)
    impact = models.CharField(max_length=30, choices=impacts)
    mitigation = models.ForeignKey(Mitigation, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=StatusList)
    last_updated = models.DateTimeField(auto_now=True)
    
    def has_view_permission(self, request, obj=None):
        return request.user.is_staff or super().has_view_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff or super().has_change_permission(request, obj)


    def __str__(self):
        return f"{self.title} reported by {self.reporter.get_full_name()}"




    
