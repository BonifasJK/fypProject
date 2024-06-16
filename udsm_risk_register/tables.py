# udsm_risk_register/tables.py
import django_tables2 as tables
from .models import RiskDetails, Mitigation, Risk

class RiskDetailsTable(tables.Table):
    class Meta:
        model = RiskDetails

class MitigationTable(tables.Table):
    class Meta:
        model = Mitigation

class RiskTable(tables.Table):
    class Meta:
        model = Risk