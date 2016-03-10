from django.db import models

# Create your models here.

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField(blank=True)
	rating = models.IntegerField()
	author = models.CharField(max_length=255)
	likes = models.
	
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(blank=True)
	question = models.IntegerField()
	author = models.CharField(max_length=255)

