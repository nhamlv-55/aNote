from django.db import models
from django import forms

# Create your models here.
from django.contrib.auth.models import User

class Vote(models.Model):
	MyoId = models.AutoField(primary_key = True)
	ArtistName = models.TextField()
	Date = models.DateField()
	Status = models.TextField()
	Bio = models.TextField()
	Image = models.URLField()
	def __unicode__(self):
		return self.ArtistName