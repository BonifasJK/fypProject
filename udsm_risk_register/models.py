from django.contrib.auth.models import AbstractUser
from django.db import models

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




class Units(models.Model):
    Unit_id = models.AutoField(primary_key=True, default=None)
    Units = models.CharField(max_length=100,choices=UnitList)
    
# Risk table added
class Risk(models.Model):
    username = models.CharField(max_length=20)
    job_title = models.CharField(max_length=20,choices=Role)
    department = models.ForeignKey(Units, on_delete=models.CASCADE)  # Link to Department model
    total_risks = models.IntegerField()
    status = models.CharField(max_length=10,choices=StatusList)
    last_updated = models.CharField(max_length=20)
    

class Risk_reported(models.Model):
    Title = models.CharField(max_length=100)
    # Reporter = models.ForeignKey(Users.Fullname,on_delete=models.CASCADE)


class User(AbstractUser):
    id = models.AutoField(primary_key=True, default=None)
    Fullname = models.CharField(max_length=200, default=None)
    Role = models.CharField(max_length=25,choices=Role, default=None)
    Unit = models.ForeignKey(Units,on_delete=models.CASCADE, default=None)
    TotalRisk = models.ForeignKey(Risk_reported,on_delete=models.CASCADE, default=None) 
    
    class Meta:
        # Specify a unique related_name for the groups field
        # This will prevent clashes with the default User model
        # You can choose any unique name you prefer
        # For example, 'custom_groups'
        db_table = 'auth_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        swappable = 'AUTH_USER_MODEL'
        ordering = ['Fullname']

    def __str__(self):
        return self.Fullname