from django.db import models

class Senate(models.Model):
  name = models.CharField(max_length=255)

class Senator(models.Model):
  senate = models.ForeignKey(Senate)
  name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  years = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)