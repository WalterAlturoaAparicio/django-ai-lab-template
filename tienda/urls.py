from django.urls import path
from .views import PokemonListView

from . import views

urlpatterns = [
    path("", PokemonListView.as_view(), name="index"),
]