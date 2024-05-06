# Generated by Django 5.0.4 on 2024-05-06 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Risk_reported',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('Unit_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Units', models.CharField(choices=[('Human Resource', 'Human Resource'), ('CoICT', 'CoICT'), ('CoET', 'CoET'), ('SoED', 'SoED'), ('CoHU', 'CoHU'), ('SoAF', 'SoAF'), ('CoAF', 'CoAF'), ('CoNAS', 'CoNAS'), ('CoSS', 'CoSS'), ('IDS', 'IDS'), ('UDSoL', 'UDSoL'), ('SJMC', 'SJMC'), ('SoMG', 'SoMG'), ('UDSE', 'UDSE'), ('IKS', 'IKS')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Fullname', models.CharField(default=None, max_length=200)),
                ('JobTitle', models.CharField(choices=[('RiskManager', 'RiskManager'), ('RiskChampion', 'RiskChampion')], default=None, max_length=25)),
                ('TotalRisk', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='udsm_risk_register.risk_reported')),
                ('Unit', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='udsm_risk_register.units')),
            ],
        ),
    ]
