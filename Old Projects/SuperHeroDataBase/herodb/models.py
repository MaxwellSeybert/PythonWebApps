from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=200)
    secretIdentity = models.CharField(max_length=200)
    weaknessess = models.TextField()
    strengths = models.TextField()
    imageLoc = models.CharField(max_length=200)
