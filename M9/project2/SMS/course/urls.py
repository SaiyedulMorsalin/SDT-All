from django.urls import path
from . import views
urlpatterns = [
    path('django/',views.course),
    path("",views.home)
]
