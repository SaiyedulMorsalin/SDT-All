from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.first_app,name='homepage'),
    path("courses",views.courses)
]
