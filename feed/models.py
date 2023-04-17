from django.db import models

# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    picture_url = models.URLField(null=True)
    created = models.DateTimeField(auto_now_add=True)
