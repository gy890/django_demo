from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=64, unique=True)
    author = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name
