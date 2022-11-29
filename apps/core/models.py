import uuid as uuid
from django.db import models
from django.utils import timezone


class TodoItem(models.Model):
    STATUS_CHOICES = (
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("on_hold", "On Hold"),
        ("done", "Done"),
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE,
                             default=None)
    title = models.CharField("Item title", max_length=255)
    description = models.TextField("Item description", blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15,
                              default="open")
    created = models.DateTimeField("Created", default=timezone.now)
    order = models.IntegerField(blank=False, default=100000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
