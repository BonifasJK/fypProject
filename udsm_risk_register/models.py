from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Count
from django.conf import settings


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
    ('Active', 'Active'),
    ('Pending', 'Pending'),
    ('Rejected', 'Rejected'),
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
    Unit_id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True, default=None)
    fullname = models.CharField(max_length=200, default=None)
    role = models.CharField(max_length=25, choices=Role, default=None)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)

    @property
    def TotalRisk(self):
        return self.risk_set.count()

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        swappable = 'AUTH_USER_MODEL'
        ordering = ['fullname']

    def __str__(self):
        return self.fullname


# Risk table added
class Risk(models.Model):
    id = models.CharField(primary_key=True, choices=ids)
    title = models.CharField(max_length=200)
    Description = models.CharField(max_length=400)
    Details = models.ForeignKey(RiskDetails, on_delete=models.CASCADE)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likelihood = models.CharField(max_length=50, choices=impacts)
    impact = models.CharField(max_length=30, choices=impacts)
    mitigation = models.ForeignKey(Mitigation, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=StatusList)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.id == 'C1':
            self.title = 'Risk1'
        elif self.id == 'C2':
            self.title = 'Risk2'
        elif self.id == 'C3':
            self.title = 'Risk2'
        elif self.id == 'C4':
            self.title = 'Risk2'
        else :
            self.title = None
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id




    
