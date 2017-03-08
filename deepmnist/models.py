from __future__ import unicode_literals

from django.db import models

# Create your models here.
class NumImage(models.Model):
    # owner = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
