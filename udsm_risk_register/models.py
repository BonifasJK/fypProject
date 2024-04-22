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


class Units(models.Model):
    Units = models.CharField(max_length=100,primary_key=True,choices=UnitList)
    

class Risk_reported(models.Model):
    Title = models.CharField(max_length=100)
    Reporter = models.ForeignKey(Users.Fullname,on_delete=models.CASCADE)


class Users(models.Model):
    Fullname = models.CharField(max_length=200,primary_key=True)
    JobTitle = models.CharField(max_length=25,choices=Role)
    Department = models.ForeignKey(Units,on_delete=models.CASCADE)
    TotalRisk = models.ForeignKey(Risk_reported,on_delete=models.CASCADE) 