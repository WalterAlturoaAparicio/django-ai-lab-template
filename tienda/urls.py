from django.urls import path

from . import views
app_name = "tienda"

urlpatterns = [
    path("", views.home, name="index"),
    path("pokemons/", views.list_pokemons, name="list_pokemons"),
    path("pokemons/<int:pk>/", views.pokemon_detail, name="pokemon_detail")
]