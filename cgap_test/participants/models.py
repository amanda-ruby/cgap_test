from django.db import models

# Create your models here.

class Participant(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    has_siblings = models.BooleanField()
