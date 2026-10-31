from django.contrib import admin
from django.urls import path
from band import views
urlpatterns=[path('admin/',admin.site.urls),path('',views.home),path('songs/',views.songs),path('photos/',views.photos),path('concerts/',views.concerts)]
