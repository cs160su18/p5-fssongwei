from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)


class Music_Playlist(models.Model):
	album_name = models.CharField(max_length=50)
	artist = models.CharField(max_length=50)

class Food_Order(models.Model):
	name = models.CharField(max_length=50)
	food = models.CharField(max_length=50)
	count = models.IntegerField()