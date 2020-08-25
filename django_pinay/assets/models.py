from django.db import models


class PinayTiktok(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()
    location = models.CharField(max_length=40)
