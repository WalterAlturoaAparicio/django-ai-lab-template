from django.urls import path

from . import views
app_name = "tienda"

urlpatterns = [
    path("", views.home, name="index"),
    # Pokemons
    path("pokemons/", views.list_pokemons, name="list_pokemons"),
    path("pokemons/<int:pk>/", views.pokemon_detail, name="pokemon_detail"),
    path("pokemons/nuevo/", views.create_pokemon, name="create_pokemon"),
    path("pokemons/<int:pk>/editar/", views.edit_pokemon, name="edit_pokemon"),
    path("pokemons/<int:pk>/eliminar/", views.delete_pokemon, name="delete_pokemon"),
    # Pedidos
    path("pedidos/", views.list_order, name="list_pedido"),
    path("pedidos/<int:pk>/", views.order_detail1, name="order_detail"),
    path("pedidos/nuevo-items/", views.create_order_items, name="create_order_items"),
    path("pedidos/<int:pk>/editar-items/", views.edit_order_items, name="edit_order"),
    path("pedidos/<int:pk>/eliminar/", views.delete_order, name="delete_order"),
    # Clientes
    path("clientes/<int:pk>/", views.trainer_detail, name="trainer_detail"),
    path("clientes/nuevo/", views.create_trainer, name="create_trainer"),
    path("clientes/<int:pk>/editar/", views.edit_trainer, name="edit_trainer"),
    path("clientes/<int:pk>/eliminar/", views.delete_trainer, name="delete_trainer"),
]