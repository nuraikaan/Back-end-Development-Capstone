from django.db import models
class Concert(models.Model):
 name=models.CharField(max_length=200); city=models.CharField(max_length=120); date=models.DateField(); tickets=models.PositiveIntegerField(default=0)
class Photo(models.Model):
 title=models.CharField(max_length=200); url=models.URLField(); event_city=models.CharField(max_length=120,blank=True)
class Song(models.Model):
 title=models.CharField(max_length=200); artist=models.CharField(max_length=200); album=models.CharField(max_length=200,blank=True); lyrics=models.TextField(blank=True)
