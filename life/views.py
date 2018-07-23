from django.shortcuts import render
from django.core import serializers
from life.models import *

def index(request):
	all_food_orders = Food_Order.objects.all()
	all_music_playlists = Music_Playlist.objects.all()
	return render(request, 'life/index.html', {"musics": all_music_playlists, "orders": all_food_orders})