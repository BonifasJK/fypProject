from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models import Count

# Create your models here.
UnitList = (
    ('Human Resource','Human Resource'),
    ('CoICT','CoICT'),
    ('CoET','CoET'),
    ('SoED','SoED'),
    ('CoHU','CoHU'),
    ('SoAF','SoAF'),
    ('CoAF','CoAF'),
    ('CoNAS','CoNAS'),
    ('CoSS','CoSS'),
    ('IDS','IDS'),
    ('UDSoL','UDSoL'),
    ('SJMC','SJMC'),
    ('SoMG','SoMG'),
    ('UDSE','UDSE'),
    ('IKS','IKS'),
)

Role = (
    ('RiskManager','RiskManager'),
    ('RiskChampion','RiskChampion'),
)

StatusList = (
    ('Active','Active'),
    ('Pending','Pending'),
    ('Rejected','Rejected'),
)


class Unit(models.Model):
    Unit_id = models.AutoField(primary_key=True)
    Units = models.CharField(max_length=100,choices=UnitList)
    
# Risk table added
class Risk(models.Model):
    reporter=models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=Role)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)  # Link to Department model
    status = models.CharField(max_length=10,choices=StatusList)
    last_updated = models.DateTimeField(auto_now=True)
    

    


class User(AbstractUser):
    id = models.AutoField(primary_key=True, default=None)
    fullname = models.CharField(max_length=200, default=None)
    role = models.CharField(max_length=25,choices=Role, default=None)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE, default=None)
    
    
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