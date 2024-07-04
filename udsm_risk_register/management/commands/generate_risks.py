import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone
from udsm_risk_register.models import Risk, User as CustomUser, RiskDetails, Mitigation
from datetime import timedelta

class Command(BaseCommand):
    help = 'Generate sample risks'

    def handle(self, *args, **kwargs):
        self.stdout.write('Generating sample risks...')

        user = CustomUser.objects.first()
        if not user:
            raise CommandError("Create a superuser before running this command!")

        now = timezone.now()
        previous_year = now - timedelta(weeks=52)

        risk_details = [
            RiskDetails.objects.create(Causes='Sample cause', consequences='Sample consequence'),
            RiskDetails.objects.create(Causes='Another cause', consequences='Another consequence')
        ]

        mitigations = [
            Mitigation.objects.create(mitigation='Sample mitigation', effectiveness='High', weakness='None'),
            Mitigation.objects.create(mitigation='Another mitigation', effectiveness='Medium', weakness='Some')
        ]

        for n in range(365):
            day = previous_year + timedelta(days=n)

            # with probability 0.5, skip creating any risk
            if random.uniform(0, 1) > 0.5:
                continue

            # create a random number of risks for this day
            num_risks = random.randint(1, 5)
            for _ in range(num_risks):
                risk = Risk.objects.create(
                    Risk_title=f'Sample Risk {_}',
                    Description='This is a sample risk description.',
                    Details=random.choice(risk_details),
                    reporter=user,
                    likelihood=random.choice(['Very High', 'High', 'Moderate', 'Low', 'Very Low']),
                    impact=random.choice(['Very High', 'High', 'Moderate', 'Low', 'Very Low']),
                    mitigation=random.choice(mitigations),
                    status=random.choice(['Submitted', 'Active', 'Pending', 'Resolved', 'Closed']),
                    last_updated=day
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated sample risks.'))
