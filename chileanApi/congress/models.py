from django.db import models

class Senate(models.Model):
  name = models.CharField(max_length=255)

class Party(model.Model):
  name = models.CharField(max_length=255)

class Circumscription(model.Model)
  number = models.IntegerField()

class Senator(models.Model):
  senate = models.ForeignKey(Senate)
  party = models.ForeignKey(Senate)
  name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  photo = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)
  years = models.CharField(max_length=255)