import os
import django
import random

# Configurar entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from tienda.models import Entrenador


def run():
    print("🔄 Borrando entrenadores anteriores...")
    Entrenador.objects.all().delete()

    entrenadores_pokemon = [
        "Ash Ketchum",
        "Misty",
        "Brock",
        "Gary Oak",
        "Serena",
        "May",
        "Dawn",
        "Cynthia",
        "Leon",
        "Iris",
        "Giovanni",
        "Red",
        "Blue",
        "Lance",
        "Steven Stone",
    ]

    dominios = ["pokemon.com", "pokeleague.com", "kanto.com"]

    for nombre in entrenadores_pokemon:
        email = f"{nombre.lower().replace(' ', '.')}" \
                f"@{random.choice(dominios)}"

        Entrenador.objects.create(
            nombre=nombre,
            email=email,
            activo=random.choice([True, True, True, False])  # mayoría activos
        )

        print(f"✅ {nombre} creado")

    print("🎉 Seed de entrenadores completado con éxito!")


if __name__ == "__main__":
    run()
