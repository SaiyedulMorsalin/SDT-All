from django.urls import path
from .import views
urlpatterns = [
    path('',views.musician_home_page,name='musician_home_page'),
    path('edit/<int:id>',views.edit_musician,name='edit_musician'),
]
