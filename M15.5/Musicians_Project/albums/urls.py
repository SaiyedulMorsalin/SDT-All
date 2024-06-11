from django.urls import path

from . import views
urlpatterns = [
    path('form/',views.album_forms,name='album_forms'),
]
