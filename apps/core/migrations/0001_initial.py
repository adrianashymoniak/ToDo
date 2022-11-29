# Generated by Django 4.1.3 on 2022-11-25 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TodoItem",
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
                ("title", models.CharField(max_length=255,
                                           verbose_name="Item title")),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Item description"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            (0, "Open"),
                            (1, "In Progress"),
                            (2, "On Hold"),
                            (3, "Done"),
                        ],
                        default=0,
                        max_length=15,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Created"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Item",
                "verbose_name_plural": "Items",
                "ordering": ["status", "title", "-created"],
            },
        ),
    ]