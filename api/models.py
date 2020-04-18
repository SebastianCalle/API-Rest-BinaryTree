from django.db import models
import uuid
import json



class BinaryTree(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = models.CharField(max_length=3000)
    created_at = models.DateTimeField('Created time', auto_now_add=True, null=True)


