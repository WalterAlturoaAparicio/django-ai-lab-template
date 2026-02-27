from django.shortcuts import get_object_or_404, render
from tienda.models import Pokemon


def home(request):
    return render(request, "tienda/home.html", {})

def list_pokemons(request):
    pokemons = Pokemon.objects.all().order_by("nombre")
    return render(request, "tienda/list_pokemons.html", {"pokemons": pokemons})

def pokemon_detail(request, pk):
    poke = get_object_or_404(Pokemon, pk=pk)
    return render(request, "tienda/pokemon_detail.html", {"pokemon": poke})
    