from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Message(models.Model):
	name = models.CharField(max_length=15)
	email = models.EmailField()
	message = models.TextField()
	
