from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.home_page),
    path('about/',views.about_page),
    path('blog/',views.blog_page),
]
