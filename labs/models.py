from django.db import models

# Create your models here.

class Lab(models.Model):
    title = models.CharField(max_length=30)
