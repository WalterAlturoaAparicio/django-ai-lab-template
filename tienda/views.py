from django.views.generic import TemplateView
import requests
import random


class PokemonListView(TemplateView):
    template_name = "tienda/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = "https://pokeapi.co/api/v2/pokemon?limit=1025"
        response = requests.get(url)
        data = response.json()

        pokemons = []

        for pokemon in data["results"]:
            pokemon_id = pokemon["url"].split("/")[-2]

            pokemons.append({
                "nombre": pokemon["name"].capitalize(),
                "precio": random.randint(100, 500),
                "imagen": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
            })

        context["pokemons"] = pokemons
        return context
