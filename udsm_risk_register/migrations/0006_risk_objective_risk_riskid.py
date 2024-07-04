# Generated by Django 5.0.6 on 2024-07-03 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udsm_risk_register', '0005_remove_risk_mitigation_risk_riskcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk',
            name='Objective',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=20, null=True, verbose_name='Objective Code'),
        ),
        migrations.AddField(
            model_name='risk',
            name='RiskID',
            field=models.CharField(max_length=20, null=True, verbose_name='Risk ID'),
        ),
    ]