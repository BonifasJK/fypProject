# Generated by Django 5.0.6 on 2024-06-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udsm_risk_register', '0004_alter_user_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='Unit_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
