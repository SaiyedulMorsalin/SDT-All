from django.urls import path
from . import views
urlpatterns = [
    path('musician/form/',views.musician_form,name='musician_form'),
]
