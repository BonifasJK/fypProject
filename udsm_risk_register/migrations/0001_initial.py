# Generated by Django 5.0.6 on 2024-06-17 11:07

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mitigation",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("mitigation", models.CharField(max_length=400)),
                ("effectiveness", models.CharField(max_length=400)),
                ("weakness", models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name="RiskDetails",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("Causes", models.CharField(max_length=400)),
                ("consequences", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                ("Unit_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "Units",
                    models.CharField(
                        choices=[
                            ("Human Resource", "Human Resource"),
                            ("CoICT", "CoICT"),
                            ("CoET", "CoET"),
                            ("SoED", "SoED"),
                            ("CoHU", "CoHU"),
                            ("SoAF", "SoAF"),
                            ("CoAF", "CoAF"),
                            ("CoNAS", "CoNAS"),
                            ("CoSS", "CoSS"),
                            ("IDS", "IDS"),
                            ("UDSoL", "UDSoL"),
                            ("SJMC", "SJMC"),
                            ("SoMG", "SoMG"),
                            ("UDSE", "UDSE"),
                            ("IKS", "IKS"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "id",
                    models.AutoField(default=None, primary_key=True, serialize=False),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("RiskManager", "RiskManager"),
                            ("RiskChampion", "RiskChampion"),
                        ],
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="udsm_risk_register.unit",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "db_table": "auth_user",
                "ordering": ["last_name", "first_name"],
                "swappable": "AUTH_USER_MODEL",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Risk",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("Description", models.CharField(max_length=400)),
                (
                    "likelihood",
                    models.CharField(
                        choices=[
                            ("Very high", "Very High"),
                            ("High", "High"),
                            ("Moderate", "Moderate"),
                            ("Low", "Low"),
                            ("Very Low", "Very Low"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "impact",
                    models.CharField(
                        choices=[
                            ("Very high", "Very High"),
                            ("High", "High"),
                            ("Moderate", "Moderate"),
                            ("Low", "Low"),
                            ("Very Low", "Very Low"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Active", "Active"),
                            ("Pending", "Pending"),
                            ("Completed", "Completed"),
                        ],
                        max_length=10,
                    ),
                ),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "mitigation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="udsm_risk_register.mitigation",
                    ),
                ),
                (
                    "reporter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "Details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="udsm_risk_register.riskdetails",
                    ),
                ),
            ],
        ),
    ]
