from django.db import models
from django.db.models import fields


# Create your models here.
class Task(models.Model):
    title = fields.CharField(max_length=40)
    description = fields.TextField(max_length=80)
    status = fields.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']
