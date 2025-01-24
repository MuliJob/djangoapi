"""API Models"""
from django.db import models

class Course(models.Model):
    """Course Model"""
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        """Returning name"""
        return self.name
