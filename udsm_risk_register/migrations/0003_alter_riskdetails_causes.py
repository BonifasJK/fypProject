# Generated by Django 5.0.6 on 2024-07-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udsm_risk_register', '0002_alter_mitigation_effectiveness_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskdetails',
            name='Causes',
            field=models.TextField(max_length=400),
        ),
    ]
