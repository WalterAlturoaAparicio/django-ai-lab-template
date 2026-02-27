import os
import django
import random
from datetime import date

# Configurar entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from tienda.models import Pedido, Entrenador, Pokemon


def run():
    print("🔄 Borrando pedidos anteriores...")
    Pedido.objects.all().delete()

    entrenadores = list(Entrenador.objects.all())
    pokemons = list(Pokemon.objects.all())

    if not entrenadores or not pokemons:
        print("❌ Necesitas primero ejecutar los seeds de Entrenador y Pokemon")
        return

    estados = ["CREADO", "PAGADO", "ENVIADO", "CERRADO"]

    total_pedidos = 20  # cantidad de pedidos a crear

    for i in range(total_pedidos):
        cliente = random.choice(entrenadores)

        pedido = Pedido.objects.create(
            cliente=cliente,
            estado=random.choice(estados),
        )

        # Agregar entre 1 y 4 pokémon aleatorios
        cantidad_pokemons = random.randint(1, 4)
        pokemons_aleatorios = random.sample(pokemons, cantidad_pokemons)

        pedido.pokemons.add(*pokemons_aleatorios)

        print(f"✅ Pedido #{pedido.id} creado para {cliente.nombre}")

    print("🎉 Seed de pedidos completado con éxito!")


if __name__ == "__main__":
    run()