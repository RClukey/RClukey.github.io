from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Picture(models.Model):
    link = models.URLField(max_length = 200)
    alt = models.TextField(blank=True)
    
    def __str__(self):
        return self.alt

class MetalEarth(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank = True)
    main_pic = models.ForeignKey(Picture, on_delete=models.PROTECT, related_name='main_sculp')
    picture = models.ManyToManyField(Picture, blank=True)

    def __str__(self):
        return self.name