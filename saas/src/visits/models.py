from django.db import models


class Visit(models.Model):
    path = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
