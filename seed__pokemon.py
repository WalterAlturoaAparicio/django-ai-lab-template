import os
import django
import requests
import random

# Configurar entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from tienda.models import Pokemon


def run():
    print("🔄 Borrando registros anteriores...")
    Pokemon.objects.all().delete()

    url = "https://pokeapi.co/api/v2/pokemon?limit=10"
    response = requests.get(url)
    data = response.json()

    for pokemon in data["results"]:
        numero = pokemon["url"].split("/")[-2]
        nombre = pokemon["name"].capitalize()
        imagen = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{numero}.png"

        Pokemon.objects.create(
            nombre=nombre,
            numero=int(numero),
            descripcion="Pokemon de la primera generación",
            precio=round(random.uniform(100, 500), 2),
            imagen=imagen
        )

        print(f"✅ {nombre} creado")

    print("🎉 Seed completado con éxito!")


if __name__ == "__main__":
    run()
