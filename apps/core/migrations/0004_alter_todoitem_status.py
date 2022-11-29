# Generated by Django 4.1.3 on 2022-11-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_todoitem_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todoitem",
            name="status",
            field=models.CharField(
                choices=[
                    ("open", "Open"),
                    ("in_progress", "In Progress"),
                    ("on_hold", "On Hold"),
                    ("done", "Done"),
                ],
                default="open",
                max_length=15,
            ),
        ),
    ]