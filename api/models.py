from django.db import models
import uuid


class BinaryTree(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = models.CharField()
    created_at = models.DateTimeField('Created time', auto_now_add=True, null=True)


