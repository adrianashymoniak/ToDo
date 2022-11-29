# Generated by Django 4.1.3 on 2022-11-28 14:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todoitem",
            name="order",
            field=models.IntegerField(default=100000),
        ),
        migrations.AddField(
            model_name="todoitem",
            name="uuid",
            field=models.UUIDField(db_index=True, default=uuid.uuid4,
                                   editable=False),
        ),
    ]