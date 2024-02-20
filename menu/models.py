# menu/models.py
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name
