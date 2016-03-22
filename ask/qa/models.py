from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(blank=True)
    rating = models.FloatField()
    author = models.ForeignKey(User)
    article_likes = models.IntegerField(default=0)

    class Meta:
        db_table = 'question'


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    class Meta:
        db_table = 'answer'


