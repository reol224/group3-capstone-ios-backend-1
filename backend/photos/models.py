from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photos(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    ts_created = models.DateTimeField(auto_now_add=True)
    ts_changed = models.DateTimeField(auto_now=False, blank=True, null=True)

    class Meta:
        db_table = 'photos'