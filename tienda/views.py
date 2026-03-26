from django.shortcuts import get_object_or_404, render, redirect
from tienda.models import Pokemon, Pedido, Entrenador
from .forms import PokemonForm


def home(request):
    return render(request, "tienda/home.html", {})


def list_pokemons(request):
    pokemons = Pokemon.objects.all().order_by("nombre")
    return render(request, "tienda/list_pokemons.html", {"pokemons": pokemons})


def pokemon_detail(request, pk):
    poke = get_object_or_404(Pokemon, pk=pk)
    return render(request, "tienda/pokemon_detail.html", {"pokemon": poke})


def order_detail1(request, pk):
    order = get_object_or_404(
        Pedido.objects.select_related("cliente").prefetch_related("pokemons"),
        pk=pk
    )
    return render(request, "tienda/order_detail.html", {"pedido": order})


def list_order(request):
    orders = Pedido.objects.select_related(
        "cliente").prefetch_related("pokemons").order_by("fecha")
    return render(request, "tienda/list_order.html", {"pedidos": orders})

def trainer_detail(request, pk):
    trainer = get_object_or_404(Entrenador.objects.prefetch_related("pedidos"), pk=pk)
    orders = trainer.pedidos.select_related("cliente").prefetch_related("pokemons").order_by("fecha")
    return render(
        request,
        "tienda/trainer_detail.html",
        {
            "entrenador": trainer,
            "pedidos": orders
        }
    )

def create_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:list_pokemons")
    else:
        form = PokemonForm()
    
    return render(request, "tienda/create_pokemon.html", {"form": form})
