from django.urls import path

from . import views
app_name = "tienda"

urlpatterns = [
    path("", views.home, name="index"),
    path("pokemons/", views.list_pokemons, name="list_pokemons"),
    path("pokemons/<int:pk>/", views.pokemon_detail, name="pokemon_detail"),
    path("pedidos/", views.list_order, name="list_pedido"),
    path("pedidos/<int:pk>/", views.order_detail1, name="order_detail"),
    path("clientes/<int:pk>/", views.trainer_detail, name="detalle_cliente"),
    path("pokemons/nuevo/", views.create_pokemon, name="create_pokemon"),
]