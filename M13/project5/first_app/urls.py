from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('about/',views.about,name='about_page'),
    path('form/',views.form_page,name='form_page'),
    path('django_form',views.django_form,name='django_form'),
]
