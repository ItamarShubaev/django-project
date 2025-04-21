

from django.urls import path
from.import views
urlpatterns = [
    path("",views.index),
    path("about-us",views.about),
    path('games/', views.game_list, name='game_list'),
]
