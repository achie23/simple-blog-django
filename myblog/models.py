from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    is_active = models.BooleanField(default=True)