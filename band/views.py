from django.conf import settings
from django.shortcuts import render
import requests
from .models import Concert,Photo,Song
def _json(url,fallback):
 try:
  r=requests.get(url,timeout=2); r.raise_for_status(); return r.json()
 except Exception: return fallback
def home(request): return render(request,'home.html',{'concerts':Concert.objects.all()})
def songs(request): return render(request,'songs.html',{'songs':_json(f'{settings.SONGS_SERVICE_URL}/song',list(Song.objects.values()))})
def photos(request): return render(request,'photos.html',{'photos':_json(f'{settings.PICTURES_SERVICE_URL}/picture',list(Photo.objects.values()))})
def concerts(request): return render(request,'concerts.html',{'concerts':Concert.objects.all()})
